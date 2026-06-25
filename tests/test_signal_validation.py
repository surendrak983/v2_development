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

from services.signal_validation_service import (
    SignalValidationService
)

service = (
    SignalValidationService()
)

service.update_future_prices()