from tempfile import gettempdir

from bse import BSE

with BSE(gettempdir()) as bse:

    methods = [
        m for m in dir(bse)
        if not m.startswith("_")
    ]

    for m in methods:
        print(m)