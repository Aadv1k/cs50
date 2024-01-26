content_types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

print(
    content_types.get(
        input("File Name: ").split(".").pop().strip().lower(),
        "application/octet-stream"))
