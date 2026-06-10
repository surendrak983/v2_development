import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from tempfile import gettempdir

from bse import BSE

with BSE(gettempdir()) as bse:

    result = bse.announcements(
        page_no=1
    )

    for item in result["Table"]:

        print(
            item["SLONGNAME"],
            "| PDFFLAG =",
            item.get("PDFFLAG"),
            "| ATTACHMENT =",
            item.get("ATTACHMENTNAME")
        )