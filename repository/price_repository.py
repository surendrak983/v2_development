"""
repository.price_repository

Maintains latest price information in RAM.

SQLite is read only during startup (or reload).
All lookups are served from memory.

Author : BSE V2
"""

from pathlib import Path
import sqlite3

from config.settings import DATABASE_DIR


class PriceRepository:
    """
    Repository for latest market prices.
    """

    _cache = {}
    _loaded = False

    DB_FILE = Path(DATABASE_DIR) / "combined_stocks.db"

    # ---------------------------------------------------------

    @classmethod
    def load(cls):
        """
        Load latest prices into RAM.
        """

        if cls._loaded:
            return

        conn = sqlite3.connect(cls.DB_FILE)
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM prices
        """)

        rows = cursor.fetchall()

        cache = {}

        for row in rows:

            record = dict(row)

            company = (
                record.get("company_name", "")
                .strip()
                .upper()
            )

            if company:
                cache[company] = record

        conn.close()

        cls._cache = cache
        cls._loaded = True

        print(f"[PriceRepository] Loaded {len(cache)} price records")

    # ---------------------------------------------------------

    @classmethod
    def reload(cls):

        cls._cache = {}
        cls._loaded = False
        cls.load()

    # ---------------------------------------------------------

    @classmethod
    def get(cls, company_name):

        if not cls._loaded:
            cls.load()

        if not company_name:
            return None

        return cls._cache.get(company_name.strip().upper())

    # ---------------------------------------------------------

    @classmethod
    def exists(cls, company_name):

        return cls.get(company_name) is not None

    # ---------------------------------------------------------

    @classmethod
    def get_ltp(cls, company_name):

        item = cls.get(company_name)

        if item is None:
            return None

        return item.get("ltp")

    # ---------------------------------------------------------

    @classmethod
    def get_previous_close(cls, company_name):

        item = cls.get(company_name)

        if item is None:
            return None

        return item.get("previous_close")

    # ---------------------------------------------------------

    @classmethod
    def get_change_percent(cls, company_name):

        item = cls.get(company_name)

        if item is None:
            return None

        return item.get("change_percent")

    # ---------------------------------------------------------

    @classmethod
    def get_volume(cls, company_name):

        item = cls.get(company_name)

        if item is None:
            return None

        return item.get("volume")

    # ---------------------------------------------------------

    @classmethod
    def get_delivery_percent(cls, company_name):

        item = cls.get(company_name)

        if item is None:
            return None

        return item.get("delivery_percent")

    # ---------------------------------------------------------

    @classmethod
    def get_market_cap(cls, company_name):

        item = cls.get(company_name)

        if item is None:
            return None

        return item.get("market_cap")

    # ---------------------------------------------------------

    @classmethod
    def update_price(
        cls,
        company_name,
        ltp=None,
        previous_close=None,
        change_percent=None,
        volume=None,
        delivery_percent=None,
        market_cap=None,
        last_updated=None,
    ):
        """
        Update only the RAM cache.
        """

        if not cls._loaded:
            cls.load()

        key = company_name.strip().upper()

        if key not in cls._cache:
            cls._cache[key] = {
                "company_name": company_name
            }

        record = cls._cache[key]

        if ltp is not None:
            record["ltp"] = ltp

        if previous_close is not None:
            record["previous_close"] = previous_close

        if change_percent is not None:
            record["change_percent"] = change_percent

        if volume is not None:
            record["volume"] = volume

        if delivery_percent is not None:
            record["delivery_percent"] = delivery_percent

        if market_cap is not None:
            record["market_cap"] = market_cap

        if last_updated is not None:
            record["last_updated"] = last_updated

    # ---------------------------------------------------------

    @classmethod
    def all(cls):

        if not cls._loaded:
            cls.load()

        return cls._cache

    # ---------------------------------------------------------

    @classmethod
    def count(cls):

        if not cls._loaded:
            cls.load()

        return len(cls._cache)