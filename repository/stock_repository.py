"""
repository.stock_repository

Central Stock Repository

Loads stock master into RAM from combined_stocks.db.

Compatible with:
    - Flask Dashboard
    - Announcement Monitor
    - MasterDataService
    - Impact Engine
    - Alpha Engine
"""

import sqlite3

from core.config import COMBINED_STOCK_DB_PATH


class StockRepository:

    _loaded = False

    _by_name = {}
    _by_symbol = {}
    _by_code = {}

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    @classmethod
    def load(cls):

        if cls._loaded:
            return

        conn = sqlite3.connect(COMBINED_STOCK_DB_PATH)
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM stocks
            """
        )

        rows = cursor.fetchall()

        conn.close()

        cls._by_name.clear()
        cls._by_symbol.clear()
        cls._by_code.clear()

        for row in rows:

            item = dict(row)

            company = (
                str(item.get("name", ""))
                .strip()
                .upper()
            )

            symbol = (
                str(item.get("symbol", ""))
                .strip()
                .upper()
            )

            security_code = (
                str(item.get("InstrmId", ""))
                .strip()
            )

            if company:
                cls._by_name[company] = item

            if symbol:
                cls._by_symbol[symbol] = item

            if security_code:
                cls._by_code[security_code] = item

        cls._loaded = True

        print(
            f"[StockRepository] Loaded {len(cls._by_name)} stocks into RAM."
        )

    # ---------------------------------------------------------

    @classmethod
    def reload(cls):

        cls._loaded = False

        cls.load()

    # ---------------------------------------------------------

    @classmethod
    def count(cls):

        cls.load()

        return len(cls._by_name)

    # ---------------------------------------------------------

    @classmethod
    def exists(cls, company_name):

        cls.load()

        if not company_name:
            return False

        return (
            company_name.strip().upper()
            in cls._by_name
        )

    # ---------------------------------------------------------

    @classmethod
    def get(cls, company_name):

        cls.load()

        if not company_name:
            return None

        return cls._by_name.get(

            company_name.strip().upper()

        )

    # ---------------------------------------------------------

    @classmethod
    def get_stock(cls, company_name):

        """
        Backward compatibility.
        """

        return cls.get(company_name)

    # ---------------------------------------------------------

    @classmethod
    def get_by_symbol(cls, symbol):

        cls.load()

        if not symbol:
            return None

        return cls._by_symbol.get(

            symbol.strip().upper()

        )

    # ---------------------------------------------------------

    @classmethod
    def get_by_security_code(cls, security_code):

        cls.load()

        if security_code is None:
            return None

        return cls._by_code.get(

            str(security_code).strip()

        )

    # ---------------------------------------------------------

    @classmethod
    def get_company_name(cls, security_code):

        stock = cls.get_by_security_code(

            security_code

        )

        if stock is None:
            return None

        return stock.get("name")

    # ---------------------------------------------------------

    @classmethod
    def get_symbol(cls, company_name):

        stock = cls.get(company_name)

        if stock is None:
            return None

        return stock.get("symbol")

    # ---------------------------------------------------------

    @classmethod
    def get_security_code(cls, company_name):

        stock = cls.get(company_name)

        if stock is None:
            return None

        return stock.get("InstrmId")

    # ---------------------------------------------------------

    @classmethod
    def get_isin(cls, company_name):

        stock = cls.get(company_name)

        if stock is None:
            return None

        return stock.get("ISIN")

    # ---------------------------------------------------------

    @classmethod
    def get_price(cls, company_name):

        stock = cls.get(company_name)

        if stock is None:
            return None

        return stock.get("ClsPric")

    # ---------------------------------------------------------

    @classmethod
    def get_volume(cls, company_name):

        stock = cls.get(company_name)

        if stock is None:
            return None

        return stock.get("TtlTradgVol")
        # ---------------------------------------------------------

    @classmethod
    def get_last_price(cls, company_name):
        """
        Backward compatibility.
        """

        return cls.get_price(company_name)

    # ---------------------------------------------------------

    @classmethod
    def get_close_price(cls, company_name):
        """
        Backward compatibility.
        """

        return cls.get_price(company_name)

    # ---------------------------------------------------------

    @classmethod
    def is_tradeable(
        cls,
        company_name=None,
        scrip_code=None,
        symbol=None,
    ):
        """
        Backward compatible tradeability check.

        Returns True if the stock exists in the master.
        """

        cls.load()

        if company_name:

            return cls.exists(company_name)

        if symbol:

            return cls.get_by_symbol(symbol) is not None

        if scrip_code:

            return cls.get_by_security_code(scrip_code) is not None

        return False

    # ---------------------------------------------------------

    @classmethod
    def get_tradingview_url(
        cls,
        company_name=None,
        symbol=None,
    ):
        """
        TradingView chart URL.
        """

        if symbol is None and company_name:

            stock = cls.get(company_name)

            if stock:

                symbol = stock.get("symbol", "")

        if not symbol:

            return ""

        symbol = str(symbol).strip().upper()

        return (
            f"https://www.tradingview.com/chart/?symbol=BSE:{symbol}"
        )

    # ---------------------------------------------------------

    @classmethod
    def get_screener_url(
        cls,
        company_name=None,
        symbol=None,
    ):
        """
        Screener.in URL.
        """

        if symbol is None and company_name:

            stock = cls.get(company_name)

            if stock:

                symbol = stock.get("symbol", "")

        if not symbol:

            return ""

        symbol = str(symbol).strip().upper()

        return (
            f"https://www.screener.in/company/{symbol}/"
        )

    # ---------------------------------------------------------

    @classmethod
    def get_all_symbols(cls):

        cls.load()

        return sorted(cls._by_symbol.keys())

    # ---------------------------------------------------------

    @classmethod
    def get_all_companies(cls):

        cls.load()

        return sorted(cls._by_name.keys())

    # ---------------------------------------------------------

    @classmethod
    def get_all_security_codes(cls):

        cls.load()

        return sorted(cls._by_code.keys())

    # ---------------------------------------------------------

    @classmethod
    def all(cls):
        """
        Returns complete RAM cache.
        """

        cls.load()

        return cls._by_name

    # ---------------------------------------------------------

    @classmethod
    def search(cls, text):
        """
        Simple company search.
        """

        cls.load()

        if not text:

            return []

        text = text.upper()

        result = []

        for company in cls._by_name:

            if text in company:

                result.append(company)

        return sorted(result)

    # ---------------------------------------------------------

    @classmethod
    def statistics(cls):

        cls.load()

        return {

            "stocks": len(cls._by_name),

            "symbols": len(cls._by_symbol),

            "security_codes": len(cls._by_code),

            "loaded": cls._loaded

        }