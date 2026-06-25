from repository.database import (
    get_connection
)

from repository.price_repository import (
    PriceRepository
)


class SignalValidationService:

    def __init__(self):

        self.price_repo = (
            PriceRepository()
        )


    def update_future_prices(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
        SELECT
            id,
            scrip_code,
            signal_date,
            price_d0
        FROM signal_performance
        WHERE price_d0 IS NOT NULL
        AND price_d1 IS NULL
        """)

        rows = cur.fetchall()

        updated = 0

        for row in rows:

            signal_id = row[0]

            scrip_code = row[1]

            signal_date = row[2]

            d0_price = row[3]

            trade_date = (
                signal_date[:10]
            )

            dates = (
                self.price_repo
                .get_next_trading_dates(
                    scrip_code,
                    trade_date,
                    limit=10
                )
            )

            if len(dates) < 10:

                continue

            try:

                d1 = self.price_repo.get_close_price(
                    scrip_code,
                    self._to_iso(
                        dates[0]
                    )
                )

                d3 = self.price_repo.get_close_price(
                    scrip_code,
                    self._to_iso(
                        dates[2]
                    )
                )

                d5 = self.price_repo.get_close_price(
                    scrip_code,
                    self._to_iso(
                        dates[4]
                    )
                )

                d10 = self.price_repo.get_close_price(
                    scrip_code,
                    self._to_iso(
                        dates[9]
                    )
                )

                r1 = (
                    (d1 - d0_price)
                    / d0_price
                ) * 100

                r3 = (
                    (d3 - d0_price)
                    / d0_price
                ) * 100

                r5 = (
                    (d5 - d0_price)
                    / d0_price
                ) * 100

                r10 = (
                    (d10 - d0_price)
                    / d0_price
                ) * 100

                cur.execute("""
                UPDATE signal_performance
                SET
                    price_d1 = ?,
                    price_d3 = ?,
                    price_d5 = ?,
                    price_d10 = ?,
                    return_d1 = ?,
                    return_d3 = ?,
                    return_d5 = ?,
                    return_d10 = ?
                WHERE id = ?
                """, (
                    d1,
                    d3,
                    d5,
                    d10,
                    r1,
                    r3,
                    r5,
                    r10,
                    signal_id
                ))

                updated += 1

            except:

                pass

        conn.commit()

        conn.close()

        print(
            f"Signals validated: {updated}"
        )


    def _to_iso(
        self,
        date_string
    ):

        day, month, year = (
            date_string.split("-")
        )

        return (
            f"{year}-{month}-{day}"
        )