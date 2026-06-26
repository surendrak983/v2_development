"""
repository.company_repository

Loads company_master.csv into RAM.

Provides fast lookup of:
- Sector
- Industry
- Market Cap
"""

from pathlib import Path
import pandas as pd
from pandas.errors import EmptyDataError


ROOT_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = ROOT_DIR / "data" / "company_master.csv"


class CompanyRepository:

    _loaded = False
    _cache = {}

    # ---------------------------------------------------------

    @classmethod
    def load(cls):

        if cls._loaded:
            return

        cls._cache = {}

        try:

            df = pd.read_csv(
                CSV_FILE,
                dtype=str
            ).fillna("")

        except (FileNotFoundError, EmptyDataError):

            print("[CompanyRepository] company_master.csv not found.")

            cls._loaded = True
            return

        for _, row in df.iterrows():

            code = str(
                row.get("scrip_code", "")
            ).strip()

            if not code:
                continue

            cls._cache[code] = {

                
                "name":
                    row.get("name", ""),
                                
                "sector":
                    row.get("sector", ""),

                "industry":
                    row.get("industry", ""),

                "market_cap":
                    row.get("market_cap", "")
            }

        cls._loaded = True

        print(
            f"[CompanyRepository] Loaded {len(cls._cache)} companies."
        )

    # ---------------------------------------------------------

    @classmethod
    def reload(cls):

        cls._loaded = False
        cls.load()

    # ---------------------------------------------------------

    @classmethod
    def get_company_info(cls, scrip_code):

        cls.load()

        return cls._cache.get(

            str(scrip_code).strip(),

            {

                "sector": "",

                "industry": "",

                "market_cap": ""

            }

        )

    # ---------------------------------------------------------

    @classmethod
    def get_sector(cls, scrip_code):

        return cls.get_company_info(

            scrip_code

        )["sector"]

    # ---------------------------------------------------------

    @classmethod
    def get_industry(cls, scrip_code):

        return cls.get_company_info(

            scrip_code

        )["industry"]

    # ---------------------------------------------------------

    @classmethod
    def get_market_cap(cls, scrip_code):

        return cls.get_company_info(

            scrip_code

        )["market_cap"]

    # ---------------------------------------------------------

    @classmethod
    def exists(cls, scrip_code):

        cls.load()

        return str(scrip_code).strip() in cls._cache

    # ---------------------------------------------------------

    @classmethod
    def count(cls):

        cls.load()

        return len(cls._cache)