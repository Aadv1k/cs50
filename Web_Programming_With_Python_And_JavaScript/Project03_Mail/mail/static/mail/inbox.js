document.addEventListener('DOMContentLoaded', function () {

    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);

    // By default, load the inbox
    load_mailbox('inbox');

    document.getElementById("compose-form").addEventListener("submit", handleMailComposition);
});

async function handleMailComposition(event) {
    event.preventDefault();
    const [mailTo, mailSubject, mailBody] =
        Array.from(document.getElementById("compose-form").querySelectorAll("input")).map(e => e.value);

    if (!mailTo.split(",").every(e => e.match(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/))) {
        return;
    }

    const res = await fetch("/emails", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            recipients: mailTo,
            subject: mailSubject,
            body: mailBody
        })
    });

    if (!res.ok) {
        return;
    }

    load_mailbox("sent");
}

function compose_email() {
    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';

    console.log("yup")
    const emailsView = document.querySelector("#emails-view");
    emailsView.innerHTML = "";

    fetch(`/emails/${mailbox}`)
        .then(res => res.json())
        .then(mails => {
            emailsView.innerHTML += `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

            for (const mail of mails) {
                const container = document.createElement("div");
                container.classList.add('list-group-item', 'px-2', 'py-1', 'list-group-item-action', `list-group-item-${mail.read ? 'light' : 'secondary'}`);
                container.setAttribute("style", "display: flex; cursor: pointer; justify-content: space-between; align-items: center");
                container.addEventListener("click", () => handleInboxItemClick(mail.id, mailbox));

                container.innerHTML = `
                    <strong>${mail.sender}</strong>
                    <div style="display: flex; gap: .5rem">
                        <p class="m-0 p-0">${mail.subject} -</p>
                        <p class="m-0 p-0 text-muted">${mail.body.length < 30 ? mail.body : mail.body.slice(30) + '...'} </p>
                    </div>
                    <p class="text-muted m-0 p-0">${mail.timestamp}</p>`;

                emailsView.appendChild(container);
            }
        });
}

async function archiveMail(id, isArchived, mailbox) {
    await fetch(`/emails/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            archived: !isArchived
        })
    });

    load_mailbox(mailbox);
}

function replyToMail(sender, subject, body, timestamp) {
    compose_email();
    document.querySelector('#compose-recipients').value = sender;
    document.querySelector('#compose-subject').value = `Re: ${subject}`;
    document.querySelector('#compose-body').value = `On ${timestamp} ${sender} wrote: ${body}`;
}

async function handleInboxItemClick(id, mailbox) {
    const res = await fetch(`/emails/${id}`);

    if (!res.ok) {
        return;
    }

    const data = await res.json();

    const emailsView = document.getElementById("emails-view");
    emailsView.innerHTML = `
        <button onclick="load_mailbox('${mailbox}')" class="mb-4 btn btn-primary">Back</button>

        ${mailbox !== "sent" ? `
            <button onclick="archiveMail('${id}', ${data.archived}, '${mailbox}')" class="mb-4 btn btn-${data.archived ? 'info' : 'secondary'}">
                ${data.archived ? 'Unarchive' : 'Archive'}
            </button>` : ''}

        <button class="mb-4 btn btn-link" onclick="replyToMail('${data.sender}', '${data.subject}', '${data.body}', '${data.timestamp}')">Reply</button>

        <div class="d-flex justify-content-between align-items-center">
            <div>
                <h2>${data.subject}</h2>
                <p class="m-0 p-0">From: <em>${data.sender}</em></p>
                <p class="m-0 p-0">To: <em>${data.recipients.join(",")}</em></p>
            </div>
            <p class="text-muted">${data.timestamp}</p>
        </div>
        <hr>
        <p>${data.body}</p>`;

    await fetch(`/emails/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            read: true
        })
    });
}
