import requests

file_name = (
    "12b079fd-9a0e-43d5-b8f2-f30ea898b3b4.pdf"
)

url = (
    "https://www.bseindia.com/"
    "xml-data/corpfiling/AttachLive/"
    f"{file_name}"
)

print("URL:", url)

response = requests.get(
    url,
    timeout=20
)

print("Status:", response.status_code)

print(
    "Content-Type:",
    response.headers.get("Content-Type")
)

if response.status_code == 200:

    with open(
        "test.pdf",
        "wb"
    ) as f:

        f.write(response.content)

    print(
        "Downloaded:",
        len(response.content),
        "bytes"
    )