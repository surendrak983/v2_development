from datetime import datetime

from market_engine.market_updater import (
    MarketUpdater
)

updater = MarketUpdater()

updater.update_date(
    datetime(2026, 6, 19)
)