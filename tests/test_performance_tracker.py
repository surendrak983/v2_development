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

from services.performance_tracker import (
    PerformanceTracker
)

tracker = PerformanceTracker()

tracker.update_d0_prices()