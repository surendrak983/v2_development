import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from repository.signal_performance_repository import (
    SignalPerformanceRepository
)

repo = SignalPerformanceRepository()

repo.save_signal(
    exchange_id="TEST001",
    scrip_code="500325",
    event_type="order_win",
    trade_signal="BUY_CANDIDATE",
    signal_date="2026-06-10"
)

for row in repo.get_all_signals():

    print(row)