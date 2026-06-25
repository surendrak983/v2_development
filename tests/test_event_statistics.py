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

from services.event_statistics_service import (
    EventStatisticsService
)

service = (
    EventStatisticsService()
)

rows = (
    service.generate_report()
)

print()

print(
    "EVENT TYPE".ljust(20),
    "COUNT".rjust(8),
    "D1".rjust(8),
    "D3".rjust(8),
    "D5".rjust(8),
    "D10".rjust(8),
    "WIN%".rjust(8)
)

print(
    "-" * 70
)

for row in rows:

    print(
        row[0].ljust(20),
        str(row[1]).rjust(8),
        str(row[2]).rjust(8),
        str(row[3]).rjust(8),
        str(row[4]).rjust(8),
        str(row[5]).rjust(8),
        str(row[6]).rjust(8)
    )