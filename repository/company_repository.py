import pandas as pd
from pathlib import Path
from pandas.errors import EmptyDataError

ROOT_DIR = Path(__file__).resolve().parent.parent

CSV_FILE = ROOT_DIR / "data" / "company_master.csv"


class CompanyRepository:

    _df = None

    @classmethod
    def _load(cls):

        if cls._df is not None:
            return

        try:

            cls._df = pd.read_csv(
                CSV_FILE,
                dtype=str
            )

        except (

            FileNotFoundError,

            EmptyDataError

        ):

            cls._df = pd.DataFrame(
                columns=[
                    "scrip_code",
                    "symbol",
                    "sector",
                    "industry",
                    "market_cap"
                ]
            )

    @classmethod
    def get_company_info(
        cls,
        scrip_code
    ):

        cls._load()

        row = cls._df.loc[
            cls._df["scrip_code"] == str(scrip_code)
        ]

        if row.empty:

            return {

                "sector": "",

                "industry": "",

                "market_cap": ""

            }

        row = row.iloc[0]

        return {

            "sector": row["sector"],

            "industry": row["industry"],

            "market_cap": row["market_cap"]

        }