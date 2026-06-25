import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from repository.price_repository import (
    PriceRepository
)

repo = PriceRepository()

price = repo.get_close_price(
    "500020",
    "2026-06-10"
)

print(price)