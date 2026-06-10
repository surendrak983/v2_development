from repository.price_repository import (
    PriceRepository
)

from repository.database import (
    get_connection
)


class PerformanceTracker:

    def __init__(self):

        self.price_repo = (
            PriceRepository()
        )

    def update_d0_prices(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
        SELECT
            id,
            scrip_code,
            signal_date
        FROM signal_performance
        WHERE price_d0 IS NULL
        """)

        rows = cur.fetchall()

        updated = 0

        for row in rows:

            signal_id = row[0]

            scrip_code = row[1]

            signal_date = row[2]

            trade_date = (
                signal_date[:10]
            )

            price = (
                self.price_repo
                .get_close_price(
                    scrip_code,
                    trade_date
                )
            )

            if price is None:

                continue

            cur.execute("""
            UPDATE signal_performance
            SET price_d0 = ?
            WHERE id = ?
            """, (
                price,
                signal_id
            ))

            updated += 1

        conn.commit()

        conn.close()

        print(
            f"D0 prices updated: {updated}"
        )