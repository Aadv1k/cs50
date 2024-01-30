from bs4 import BeautifulSoup, Tag
from urllib.parse import urlparse
import re
from datetime import datetime

import requests
import os
import pickle

import hashlib


def str_to_md5(s: str) -> str:
    h = hashlib.md5(s.encode())
    return h.hexdigest()



class Assignment:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")

    @property
    def title(self):
        title_element = self.soup.find(
            "div", class_="font-weight-bold text-uppercase mb-1 text-gray-800"
        )
        return title_element.text.strip() if title_element else None

    def __parse_date_dirty(self, s):
        return datetime.strptime(
            re.sub(r"(\s+)|IST (\(.*\))", " ",
                   s[s.find(":") + 1:].strip()).strip(),
            "%d %b %Y %I:%M %p",
        )

    @property
    def start_time(self):
        return self.__parse_date_dirty(
            self.soup.select("div.mb-0.text-gray-800")[0].text
        )

    @property
    def end_time(self):
        return self.__parse_date_dirty(
            self.soup.select("div.mb-0.text-gray-800")[1].text
        )

    def __str__(self):
        return f"{self.title} starts at {self.start_time}"

    @staticmethod
    def get_pdf_id_from_url(url):
        parsed_url = urlparse(url)
        id = parsed_url.path.split("/").pop()
        return id

    @property
    def attached_pdf_url(self):
        url = self.soup.select_one('a[href*="/v1/studentweb/readpdf/"]')
        if not url:
            return None
        id = Assignment.get_pdf_id_from_url(url["href"])
        return f"https://teach.practically.com/v1/files/shared/content/{id[:2]}/{id}/{id}.pdf"


class Assignments:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")
        self.items = []
        self.__populate_with()

    def __populate_with(self):
        for child in self.soup.select(
                "div > div > div.card.h-100 > div.card-body"):
            self.items.append(Assignment(str(child)))

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)


class Classroom:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")

    @property
    def name(self):
        return self.soup.find(
            "div", class_="font-weight-bold").text.strip() or None

    @property
    def owner(self):
        return self.soup.find("div", class_="mb-0").text.strip() or None

    @property
    def id(self):
        return self.soup.find("a")["href"].split("/").pop() or None


class Classrooms:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")
        self.items = []
        self.__populate_with()

    def __populate_with(self):
        for elem in self.soup.find_all("div", class_="col-xl-3 col-md-6 mb-4"):
            self.items.append(Classroom(str(elem)))

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)


class User:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, 'html.parser')

    @property
    def email(self) -> str | None:
        html_input_elem = self.soup.find("input", {"id": "Email"})
        return html_input_elem['value'] if html_input_elem else None

    @property
    def first_name(self) -> str | None:
        html_input_elem = self.soup.find("input", {"id": "FirstName"})
        return html_input_elem['value'] if html_input_elem else None

    @property
    def last_name(self) -> str | None:
        html_input_elem = self.soup.find("input", {"id": "LastName"})
        return html_input_elem['value'] if html_input_elem else None

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Practically:
    def __init__(
        self, base_url="https://teach.practically.com", session_file="session.pickle"
    ):
        self.base_url = base_url
        self.session_id = None
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"
        self.session_file = session_file

    def __dump_session(self):
        with open(self.session_file, "wb") as f:
            pickle.dump({"session_id": self.session_id}, f)

    def __load_session(self):
        try:
            with open(self.session_file, "rb") as f:
                data = pickle.load(f)
                session_id = data.get("session_id")

                if not session_id:
                    raise Exception

                return session_id
        except BaseException:
            return None

    def is_session_expired_or_invalid(self):
        try:
            res = requests.get(
                f"{self.base_url}/v1/studentweb/myschool/dashboard",
                headers={"Cookie": f"ci_session={self.session_id}"},
            )
            res.raise_for_status()
            return not res.ok
        except requests.RequestException:
            return True

    def create_session(self, username, password):
        found = self.__load_session()

        if not found or self.is_session_expired_or_invalid():
            res = requests.post(
                f"{self.base_url}/v1/teacherapp_v1/loginWithPassword",
                headers={
                    "User-Agent": self.user_agent,
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                data={
                    "LoginID": username,
                    "Password": str_to_md5(password),
                    "IsWebRequest": "Y",
                },
            )

            session_id = res.cookies.get("ci_session")

            self.session_id = session_id
            self.__dump_session()
        else:
            self.session_id = found

    def __get_secure(self, url):
        res = requests.get(
            f"{self.base_url}{url}", headers={"Cookie": f"ci_session={self.session_id}"}
        )
        return res.text if res.status_code == 200 else None

    def get_user(self):
        return User(self.__get_secure("/v1/studentweb/profile"))

    def get_classrooms(self):
        return Classrooms(self.__get_secure("/v1/studentweb/myschool/classes"))

    def get_assignments(self, classroom_id):
        return Assignments(
            self.__get_secure(
                f"/v1/studentweb/classdetail/{classroom_id}/assignments")
        )

    def create_session_from_env(self, username_var, password_var):
        return self.create_session(
            os.getenv(username_var), os.getenv(password_var))

def main():
    print("yo this works!")

if __name__ == "__main__":
    main()
