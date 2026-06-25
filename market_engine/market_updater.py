from datetime import datetime, timedelta
import csv
import io

from market_engine.market_database import (
    get_connection,
    initialize_database
)

from market_engine.bhavcopy_downloader import (
    BhavcopyDownloader
)


UPSERT_SQL = """
INSERT OR REPLACE INTO bse_cash_eod (

    trade_date,
    fininstrm_id,
    symbol,
    isin,
    open_price,
    high_price,
    low_price,
    close_price,
    last_price,
    prev_close,
    volume,
    turnover,
    trades,
    downloaded_at

)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""


class MarketUpdater:

    def __init__(self):

        initialize_database()

        self.downloader = BhavcopyDownloader()

    def to_int(self, value):

        if value in (None, ""):
            return None

        return int(float(value))

    def to_float(self, value):

        if value in (None, ""):
            return None

        return float(value)

    def normalize_rows(
            self,
            csv_text,
            trade_date):

        reader = csv.DictReader(
            io.StringIO(csv_text)
        )

        stamp = datetime.now().isoformat(
            timespec="seconds"
        )

        rows = []

        for raw in reader:

            rows.append(
                (
                    trade_date.strftime("%d-%m-%Y"),

                    self.to_int(
                        raw["FinInstrmId"]
                    ),

                    raw.get("TckrSymb"),

                    raw.get("ISIN"),

                    self.to_float(
                        raw.get("OpnPric")
                    ),

                    self.to_float(
                        raw.get("HghPric")
                    ),

                    self.to_float(
                        raw.get("LwPric")
                    ),

                    self.to_float(
                        raw.get("ClsPric")
                    ),

                    self.to_float(
                        raw.get("LastPric")
                    ),

                    self.to_float(
                        raw.get("PrvsClsgPric")
                    ),

                    self.to_int(
                        raw.get("TtlTradgVol")
                    ),

                    self.to_float(
                        raw.get("TtlTrfVal")
                    ),

                    self.to_int(
                        raw.get(
                            "TtlNbOfTxsExctd"
                        )
                    ),

                    stamp
                )
            )

        return rows

    def save_rows(
            self,
            trade_date,
            rows):

        with get_connection() as conn:

            conn.execute(
                """
                DELETE FROM bse_cash_eod
                WHERE trade_date=?
                """,
                (
                    trade_date.strftime(
                        "%d-%m-%Y"
                    ),
                )
            )

            conn.executemany(
                UPSERT_SQL,
                rows
            )

    def update_date(
            self,
            trade_date):

        csv_text = self.downloader.download_csv(
            trade_date
        )

        if not csv_text:

            return

        rows = self.normalize_rows(
            csv_text,
            trade_date
        )

        self.save_rows(
            trade_date,
            rows
        )

        print(
            f"{trade_date:%d-%m-%Y} "
            f"Rows saved: {len(rows)}"
        )

    def update_today(self):

        self.update_date(
            datetime.now()
        )

    def update_range(
            self,
            start_date,
            end_date):

        current = start_date

        while current <= end_date:

            self.update_date(current)

            current += timedelta(days=1)