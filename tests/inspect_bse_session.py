from tempfile import gettempdir

from bse import BSE

with BSE(gettempdir()) as bse:

    print(type(bse.session))

    print(bse.session.headers)