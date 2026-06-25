from repository.database import get_connection


class AdaptiveScoringEngine:

    def get_adjustment(
        self,
        event_type
    ):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute(
            """
            SELECT

                COUNT(*) AS total_signals,

                AVG(return_d5),

                ROUND(
                    100.0 *
                    SUM(
                        CASE
                            WHEN return_d5 > 0
                            THEN 1
                            ELSE 0
                        END
                    )
                    /
                    COUNT(return_d5),
                    2
                )

            FROM signal_performance

            WHERE

                event_type = ?

                AND return_d5 IS NOT NULL
            """,
            (
                event_type,
            )
        )

        row = cur.fetchone()

        conn.close()

        count = row[0]
        avg_return = row[1]
        win_rate = row[2]

        if avg_return is None:

            return 0

        adjustment = 0

        #
        # Win-rate based adjustment
        #

        if win_rate >= 80:

            adjustment += 10

        elif win_rate >= 60:

            adjustment += 5

        elif win_rate < 40:

            adjustment -= 10

        #
        # Return based adjustment
        #

        if avg_return >= 10:

            adjustment += 10

        elif avg_return >= 5:

            adjustment += 5

        elif avg_return <= -5:

            adjustment -= 5

        #
        # Sample size penalty
        #

        if count < 5:

            adjustment -= 5

        return adjustment