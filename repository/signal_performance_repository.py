from repository.database import get_connection


class SignalPerformanceRepository:

    def save_signal(
        self,
        exchange_id,
        scrip_code,
        event_type,
        trade_signal,
        signal_date
    ):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        INSERT OR IGNORE INTO signal_performance
        (
            exchange_id,
            scrip_code,
            event_type,
            trade_signal,
            signal_date
        )
        VALUES
        (
            ?, ?, ?, ?, ?
        )
        """,
        (
            exchange_id,
            scrip_code,
            event_type,
            trade_signal,
            signal_date
        ))

        conn.commit()
        conn.close()


    def get_all_signals(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        SELECT *
        FROM signal_performance
        ORDER BY id DESC
        """)

        rows = cur.fetchall()

        conn.close()

        return rows