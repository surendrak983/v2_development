from tempfile import gettempdir
from pprint import pprint

from bse import BSE

with BSE(gettempdir()) as bse:

    result = bse.announcements(
        page_no=1
    )

    items = result.get(
        "Table",
        []
    )

    for item in items:

        if item.get(
            "ATTACHMENTNAME"
        ):

            pprint(item)

            break