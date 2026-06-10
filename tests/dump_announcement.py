import sys
from pathlib import Path
from pprint import pprint

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

    pprint(
        result["Table"][0]
    )