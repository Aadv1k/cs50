from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest

from . import util
import random

def random_entry(request):
    return redirect(f"wiki/{random.choice(util.list_entries())}")

def edit_entry(request, entry_name: str):
    entry_content = util.get_entry(entry_name)
    return render(request, "encyclopedia/edit_entry.html", {
        "entry_title": entry_name,
        "entry_content": entry_content
    })


def new_entry(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/new_entry.html")

    e_title = request.POST.get("entry_title")
    e_content = request.POST.get("entry_content")

    if not e_title or not e_content:
      return HttpResponseBadRequest("Either the title or the content were found to be missing")

    if not request.POST.get("editing") and (util.get_entry(e_title) is not None):
        return HttpResponseBadRequest("Entry already exists, use some other name")

    util.save_entry(e_title, e_content)
    return redirect(f"/wiki/{e_title}")

def index(request):
    query = request.GET.get("q")
    entries = util.list_entries()

    if query is None:
        return render(request, "encyclopedia/index.html", {
            "entries": entries
        })

    if util.get_entry(query) is not None:
        return redirect(f"wiki/{query.lower()}")

    entries = list(filter(lambda entry: query.lower() in entry.lower(), entries))
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })



def entry(request, entry_name: str):
    found_entry = util.get_entry(entry_name)
    if found_entry is None:
        return render(request, "encyclopedia/error.html", {
            "error_desc": f"Was unable to find \"{entry_name}\", it probably doesn't exist",
            "error_name": "Entry not found"
        }, status=404)

    html_content = util.markdown_to_html(found_entry)

    return render(request, "encyclopedia/entry.html", {
        "entry_title": entry_name,
        "entry_content": html_content
    })

