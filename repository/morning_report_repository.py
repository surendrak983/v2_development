from repository.database import get_connection


class MorningReportRepository:

    def get_latest_announcements(
        self,
        limit=100
    ):

        conn = get_connection()

        conn.row_factory = (
            lambda cursor, row: {
                column[0]: row[index]
                for index, column
                in enumerate(cursor.description)
            }
        )

        cur = conn.cursor()

        cur.execute("""
        WITH latest_analysis AS (
            SELECT ar.*
            FROM analysis_results ar
            JOIN (
                SELECT
                    exchange_id,
                    MAX(id) AS latest_id
                FROM analysis_results
                GROUP BY exchange_id
            ) latest
                ON latest.latest_id = ar.id
        )
        SELECT
            a.exchange_id,
            a.scrip_code,
            a.company_name,
            a.headline,
            a.announcement_time,
            a.created_at,
            la.event_type,
            la.confidence,
            la.impact_score,
            la.impact_signal,
            la.trade_signal,
            la.priority
        FROM announcements a
        LEFT JOIN latest_analysis la
            ON la.exchange_id = a.exchange_id
        ORDER BY
            a.announcement_time DESC,
            a.id DESC
        LIMIT ?
        """, (
            limit,
        ))

        rows = cur.fetchall()

        conn.close()

        return rows

    def get_high_priority_announcements(
        self,
        limit=25
    ):

        conn = get_connection()

        conn.row_factory = (
            lambda cursor, row: {
                column[0]: row[index]
                for index, column
                in enumerate(cursor.description)
            }
        )

        cur = conn.cursor()

        cur.execute("""
        WITH latest_analysis AS (
            SELECT ar.*
            FROM analysis_results ar
            JOIN (
                SELECT
                    exchange_id,
                    MAX(id) AS latest_id
                FROM analysis_results
                GROUP BY exchange_id
            ) latest
                ON latest.latest_id = ar.id
        )
        SELECT
            a.exchange_id,
            a.scrip_code,
            a.company_name,
            a.headline,
            a.announcement_time,
            a.created_at,
            la.event_type,
            la.confidence,
            la.impact_score,
            la.impact_signal,
            la.trade_signal,
            la.priority
        FROM announcements a
        JOIN latest_analysis la
            ON la.exchange_id = a.exchange_id
        WHERE la.priority <= 3
        ORDER BY
            la.priority ASC,
            la.impact_score DESC,
            a.announcement_time DESC
        LIMIT ?
        """, (
            limit,
        ))

        rows = cur.fetchall()

        conn.close()

        return rows

    def get_signal_counts(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
        SELECT
            COALESCE(trade_signal, 'UNANALYZED') AS trade_signal,
            COUNT(*)
        FROM analysis_results
        GROUP BY trade_signal
        ORDER BY COUNT(*) DESC
        """)

        rows = cur.fetchall()

        conn.close()

        return dict(rows)
