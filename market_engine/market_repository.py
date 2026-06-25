# market_engine/market_repository.py

from datetime import datetime

from market_engine.market_database import get_connection


class MarketRepository:

    def normalize_date(self, trade_date):
        """
        Convert YYYY-MM-DD to DD-MM-YYYY.
        Leave DD-MM-YYYY unchanged.
        """

        if trade_date is None:
            return None

        trade_date = str(trade_date)[:10]

        try:

            if len(trade_date) >= 10 and trade_date[4] == "-":

                return (
                    datetime
                    .strptime(
                        trade_date,
                        "%Y-%m-%d"
                    )
                    .strftime("%d-%m-%Y")
                )

            return trade_date

        except Exception:

            return trade_date

    def get_close_price(
        self,
        scrip_code,
        trade_date
    ):
        """
        Get closing price for a given date.
        """

        trade_date = self.normalize_date(trade_date)

        with get_connection() as conn:

            cur = conn.cursor()

            cur.execute(
                """
                SELECT close_price
                FROM bse_cash_eod
                WHERE
                    fininstrm_id = ?
                    AND trade_date = ?
                """,
                (
                    str(scrip_code),
                    trade_date
                )
            )

            row = cur.fetchone()

        if row:
            return row["close_price"]

        return None

    def get_nth_trading_day_price(
        self,
        scrip_code,
        signal_date,
        n
    ):
        """
        Get closing price after N trading days.
        """

        signal_date = self.normalize_date(signal_date)

        with get_connection() as conn:

            cur = conn.cursor()

            cur.execute(
                """
                SELECT
                    trade_date,
                    close_price
                FROM bse_cash_eod
                WHERE
                    fininstrm_id = ?
                    AND
                    substr(trade_date,7,4)
                    ||
                    substr(trade_date,4,2)
                    ||
                    substr(trade_date,1,2)
                    >
                    substr(?,7,4)
                    ||
                    substr(?,4,2)
                    ||
                    substr(?,1,2)

                ORDER BY
                    substr(trade_date,7,4),
                    substr(trade_date,4,2),
                    substr(trade_date,1,2)

                LIMIT 1
                OFFSET ?
                """,
                (
                    str(scrip_code),
                    signal_date,
                    signal_date,
                    signal_date,
                    n - 1
                )
            )

            row = cur.fetchone()

        if row:
            return row["close_price"]

        return None

    def get_price_series(
        self,
        scrip_code,
        start_date=None,
        end_date=None
    ):
        """
        Get historical price series.
        """

        query = """
        SELECT
            trade_date,
            close_price
        FROM bse_cash_eod
        WHERE
            fininstrm_id = ?
        """

        params = [str(scrip_code)]

        if start_date:

            start_date = self.normalize_date(start_date)

            query += """
            AND
                substr(trade_date,7,4)
                ||
                substr(trade_date,4,2)
                ||
                substr(trade_date,1,2)
                >=
                substr(?,7,4)
                ||
                substr(?,4,2)
                ||
                substr(?,1,2)
            """

            params.extend(
                [
                    start_date,
                    start_date,
                    start_date
                ]
            )

        if end_date:

            end_date = self.normalize_date(end_date)

            query += """
            AND
                substr(trade_date,7,4)
                ||
                substr(trade_date,4,2)
                ||
                substr(trade_date,1,2)
                <=
                substr(?,7,4)
                ||
                substr(?,4,2)
                ||
                substr(?,1,2)
            """

            params.extend(
                [
                    end_date,
                    end_date,
                    end_date
                ]
            )

        query += """
        ORDER BY
            substr(trade_date,7,4),
            substr(trade_date,4,2),
            substr(trade_date,1,2)
        """

        with get_connection() as conn:

            cur = conn.cursor()

            cur.execute(
                query,
                tuple(params)
            )

            rows = cur.fetchall()

        return rows