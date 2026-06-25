
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

from repository.database import get_connection
from services.analysis_service import AnalysisService

service = AnalysisService()

conn = get_connection()
cur = conn.cursor()

cur.execute("""
SELECT

    a.exchange_id,

    a.scrip_code,

    a.headline,

    t.raw_text

FROM announcements a

LEFT JOIN
(
    SELECT
        scrip_code,
        MAX(id) AS max_id
    FROM attachment_texts
    GROUP BY scrip_code
)
latest

ON a.scrip_code = latest.scrip_code

LEFT JOIN attachment_texts t

ON t.id = latest.max_id
""")

rows = cur.fetchall()

processed = 0

for (
    exchange_id,
    scrip_code,
    headline,
    raw_text
) in rows:

    try:

        service.analyze_and_store(
            exchange_id=exchange_id,
            headline=headline,
            pdf_text=raw_text
        )

        processed += 1

    except Exception as e:

        print(
            exchange_id,
            e
        )

conn.close()

print()
print(
    f"Processed {processed} announcements"
)

