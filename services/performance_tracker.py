
from repository.database import (
    get_connection
)

from repository.price_repository import (
    PriceRepository
)


class PerformanceTracker:

    def __init__(self):

        self.price_repo = (
            PriceRepository()
        )

    def update_d0_prices(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute(
        """
        SELECT

            id,
            scrip_code,
            signal_date

        FROM signal_performance

        WHERE price_d0 IS NULL
        """
        )

        rows = cur.fetchall()

        updated = 0

        for signal_id, scrip_code, signal_date in rows:

            trade_date = (
                signal_date[:10]
            )

            price_d0 = (
                self.price_repo
                .get_close_price(
                    scrip_code,
                    trade_date
                )
            )

            if price_d0 is None:

                continue

            cur.execute(
            """
            UPDATE signal_performance
            SET price_d0=?
            WHERE id=?
            """,
            (
                price_d0,
                signal_id
            )
            )

            updated += 1

        conn.commit()

        conn.close()

        print(
            f"D0 prices updated: {updated}"
        )

    def update_returns(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute(
        """
        SELECT

            id,
            scrip_code,
            signal_date,
            price_d0

        FROM signal_performance

        WHERE price_d0 IS NOT NULL
        """
        )

        rows = cur.fetchall()

        updated = 0

        for (
            signal_id,
            scrip_code,
            signal_date,
            price_d0
        ) in rows:

            price_d1 = (
                self.price_repo
                .get_nth_trading_day_price(
                    scrip_code,
                    signal_date,
                    1
                )
            )

            price_d3 = (
                self.price_repo
                .get_nth_trading_day_price(
                    scrip_code,
                    signal_date,
                    3
                )
            )

            price_d5 = (
                self.price_repo
                .get_nth_trading_day_price(
                    scrip_code,
                    signal_date,
                    5
                )
            )

            price_d10 = (
                self.price_repo
                .get_nth_trading_day_price(
                    scrip_code,
                    signal_date,
                    10
                )
            )

            return_d1 = None
            return_d3 = None
            return_d5 = None
            return_d10 = None

            if price_d1:

                return_d1 = (
                    (
                        price_d1
                        -
                        price_d0
                    )
                    /
                    price_d0
                ) * 100

            if price_d3:

                return_d3 = (
                    (
                        price_d3
                        -
                        price_d0
                    )
                    /
                    price_d0
                ) * 100

            if price_d5:

                return_d5 = (
                    (
                        price_d5
                        -
                        price_d0
                    )
                    /
                    price_d0
                ) * 100

            if price_d10:

                return_d10 = (
                    (
                        price_d10
                        -
                        price_d0
                    )
                    /
                    price_d0
                ) * 100

            cur.execute(
            """
            UPDATE signal_performance

            SET

                price_d1=?,
                price_d3=?,
                price_d5=?,
                price_d10=?,

                return_d1=?,
                return_d3=?,
                return_d5=?,
                return_d10=?

            WHERE id=?
            """,
            (
                price_d1,
                price_d3,
                price_d5,
                price_d10,

                return_d1,
                return_d3,
                return_d5,
                return_d10,

                signal_id
            )
            )

            updated += 1

        conn.commit()

        conn.close()

        print(
            f"Returns updated: {updated}"
        )

    def update_all(self):

        self.update_d0_prices()

        self.update_returns()

