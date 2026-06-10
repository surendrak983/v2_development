import sys
from pathlib import Path

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from repository.database import (
    get_connection
)

conn = get_connection()

cur = conn.cursor()

cur.execute("""
SELECT
    id,
    scrip_code,
    signal_date
FROM signal_performance
ORDER BY id DESC
LIMIT 20
""")

for row in cur.fetchall():

    print(row)

conn.close()