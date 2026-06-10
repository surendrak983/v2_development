from tempfile import gettempdir
from bse import BSE

print("Starting...")

with BSE(gettempdir()) as bse:

    print("Connected")

    result = bse.announcements(
        page_no=1
    )

    print("Received result")

    print(type(result))