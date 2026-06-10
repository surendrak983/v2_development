from tempfile import gettempdir

from bse import BSE

ATTACHMENT = (
    "12b079fd-9a0e-43d5-b8f2-f30ea898b3b4.pdf"
)

URL = (
    "https://www.bseindia.com/xml-data/"
    "corpfiling/AttachLive/"
    + ATTACHMENT
)

with BSE(gettempdir()) as bse:

    response = bse.session.get(
        URL,
        timeout=30
    )

    print(
        "Status:",
        response.status_code
    )

    print(
        "Content-Type:",
        response.headers.get(
            "Content-Type"
        )
    )

    if response.status_code == 200:

        with open(
            "test.pdf",
            "wb"
        ) as f:

            f.write(
                response.content
            )

        print(
            "PDF saved"
        )