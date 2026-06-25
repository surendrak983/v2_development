
from repository.database import get_connection


class StatisticsEngine:

    def get_total_announcements(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM analysis_results
            """
        )

        total = cursor.fetchone()[0]

        conn.close()

        return total

    def get_event_counts(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                event_type,
                COUNT(*)
            FROM analysis_results
            GROUP BY event_type
            ORDER BY COUNT(*) DESC
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return dict(rows)

    def get_average_alpha_score(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT AVG(alpha_score)
            FROM analysis_results
            WHERE alpha_score IS NOT NULL
            """
        )

        avg_score = cursor.fetchone()[0]

        conn.close()

        if avg_score is None:

            return 0

        return round(avg_score, 2)

    def get_alpha_signal_counts(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
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

        rows = cursor.fetchall()

        conn.close()

        return {
            row[0]: row[1]
            for row in rows
        }

    def get_trade_signal_counts(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                trade_signal,
                COUNT(*)
            FROM analysis_results
            GROUP BY trade_signal
            ORDER BY COUNT(*) DESC
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return dict(rows)

    def get_average_alpha_by_event(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
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

        rows = cursor.fetchall()

        conn.close()

        return {
            row[0]: round(row[1], 2)
            for row in rows
        }

    def get_strong_buy_count(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM analysis_results
            WHERE alpha_signal = 'STRONG_BUY'
            """
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count

    def get_buy_count(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM analysis_results
            WHERE alpha_signal = 'BUY'
            """
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count

