from market_engine.market_repository import (
    MarketRepository
)


class PriceRepository(MarketRepository):
    """
    Compatibility wrapper.

    Existing code can continue using
    PriceRepository without modification.
    """
    pass