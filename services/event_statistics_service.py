from repository.database import (
    get_connection
)


class EventStatisticsService:

    def generate_report(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
SELECT
    event_type,

    COUNT(*) AS total_signals,

    ROUND(AVG(return_d1),2),

    ROUND(AVG(return_d3),2),

    ROUND(AVG(return_d5),2),

    ROUND(AVG(return_d10),2),

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
    return_d1 IS NOT NULL
    OR return_d3 IS NOT NULL
    OR return_d5 IS NOT NULL

GROUP BY event_type

ORDER BY
    AVG(return_d5) DESC
""")

        rows = cur.fetchall()

        conn.close()

        return rows