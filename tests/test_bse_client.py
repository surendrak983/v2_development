import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from integrations.bse_client import (
    BSEClient
)

client = BSEClient()

items = client.get_announcements()

print(
    f"Announcements: {len(items)}"
)

for item in items[:5]:

    print()

    print(
        item["company_name"]
    )

    print(
        item["headline"]
    )