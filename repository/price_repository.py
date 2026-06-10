import sqlite3

from datetime import datetime

from core.config import (
    MARKET_DATA_DB_PATH
)


class PriceRepository:

    def get_close_price(
        self,
        scrip_code,
        trade_date
    ):

        formatted_date = (
            datetime.strptime(
                trade_date,
                "%Y-%m-%d"
            )
            .strftime(
                "%d-%m-%Y"
            )
        )

        conn = sqlite3.connect(
            MARKET_DATA_DB_PATH
        )

        cur = conn.cursor()

        cur.execute("""
        SELECT
            close_price
        FROM bse_cash
        WHERE fininstrm_id = ?
        AND trade_date = ?
        """, (
            int(scrip_code),
            formatted_date
        ))

        row = cur.fetchone()

        conn.close()

        if row is None:

            return None

        return row[0]