from repository.database import get_connection
from utils.time_utils import utc_to_ist


class DashboardDataService:

    def get_summary(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT COUNT(*)
            FROM analysis_results
            """
        )
        total_announcements = cur.fetchone()[0]

        cur.execute(
            """
            SELECT AVG(alpha_score)
            FROM analysis_results
            WHERE alpha_score IS NOT NULL
            """
        )
        avg_alpha = cur.fetchone()[0]

        if avg_alpha is None:
            avg_alpha = 0

        cur.execute(
            """
            SELECT COUNT(*)
            FROM analysis_results
            WHERE alpha_signal='STRONG_BUY'
            """
        )
        strong_buy_count = cur.fetchone()[0]

        cur.execute(
            """
            SELECT COUNT(*)
            FROM analysis_results
            WHERE alpha_signal='BUY'
            """
        )
        buy_count = cur.fetchone()[0]

        conn.close()

        return {

            "total_announcements": total_announcements,

            "average_alpha": round(
                avg_alpha,
                2
            ),

            "strong_buy_count": strong_buy_count,

            "buy_count": buy_count

        }

    def get_recent_announcements(
        self,
        limit=100
    ):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT

                a.created_at,

                b.company_name,

                b.scrip_code,

                b.headline,

                a.event_type,

                a.impact_score,

                a.alpha_score,

                a.alpha_signal

            FROM analysis_results a

            INNER JOIN announcements b

            ON a.exchange_id=b.exchange_id

            ORDER BY a.id DESC

            LIMIT ?
            """,

            (limit,)
        )

        rows = cur.fetchall()

        conn.close()

        rows = [

            (
                utc_to_ist(row[0]),
                *row[1:]
            )

            for row in rows

        ]

        return rows

    def get_strong_buy(
        self,
        min_alpha=90
    ):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT

                a.created_at,

                b.company_name,

                b.scrip_code,

                b.headline,

                a.event_type,

                a.impact_score,

                a.alpha_score,

                a.alpha_signal

            FROM analysis_results a

            INNER JOIN announcements b

            ON a.exchange_id=b.exchange_id

            WHERE

                a.alpha_score >= ?

            ORDER BY a.id DESC
            """,

            (min_alpha,)
        )

        rows = cur.fetchall()

        conn.close()

        rows = [

            (
                utc_to_ist(row[0]),
                *row[1:]
            )

            for row in rows

        ]

        return rows

    def get_action_center(
        self,
        min_alpha=90
    ):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT

                a.created_at,

                b.company_name,

                b.scrip_code,

                b.headline,

                a.event_type,

                a.impact_score,

                a.alpha_score,

                a.alpha_signal,

                c.pdf_file

            FROM analysis_results a

            INNER JOIN announcements b

            ON a.exchange_id=b.exchange_id

            LEFT JOIN attachment_texts c

            ON b.scrip_code=c.scrip_code

            WHERE

                a.alpha_signal='STRONG_BUY'

                AND

                a.alpha_score>=?

            ORDER BY a.id DESC
            """,

            (min_alpha,)
        )

        rows = cur.fetchall()

        conn.close()

        rows = [

            (
                utc_to_ist(row[0]),
                *row[1:]
            )

            for row in rows

        ]

        return rows

    def get_event_counts(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT

                event_type,

                COUNT(*)

            FROM analysis_results

            GROUP BY event_type

            ORDER BY COUNT(*) DESC
            """
        )

        rows = cur.fetchall()

        conn.close()

        return rows

    def get_alpha_signal_counts(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT

                alpha_signal,

                COUNT(*)

            FROM analysis_results

            WHERE alpha_signal IS NOT NULL

            GROUP BY alpha_signal

            ORDER BY COUNT(*) DESC
            """
        )

        rows = cur.fetchall()

        conn.close()

        return rows

    def get_average_alpha_by_event(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT

                event_type,

                AVG(alpha_score)

            FROM analysis_results

            WHERE alpha_score IS NOT NULL

            GROUP BY event_type

            ORDER BY AVG(alpha_score) DESC
            """
        )

        rows = cur.fetchall()

        conn.close()

        return rows