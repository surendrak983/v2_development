from market_engine.market_repository import (
    MarketRepository
)

from market_engine.market_updater import (
    MarketUpdater
)


class MarketService:

    def __init__(self):

        self.repo = MarketRepository()

        self.updater = MarketUpdater()