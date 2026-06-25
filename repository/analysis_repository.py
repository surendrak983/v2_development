
from repository.database import get_connection


def save_analysis(
    exchange_id,
    event_type,
    confidence,
    impact_score,
    impact_signal,
    trade_signal,
    priority,
    alpha_score,
    alpha_signal
):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        """
        SELECT 1
        FROM analysis_results
        WHERE exchange_id = ?
        """,
        (
            exchange_id,
        )
    )

    if cur.fetchone():

        conn.close()

        return False

    cur.execute(
        """
        INSERT INTO analysis_results
        (
            exchange_id,
            event_type,
            confidence,
            impact_score,
            impact_signal,
            trade_signal,
            priority,
            alpha_score,
            alpha_signal
        )
        VALUES
        (
            ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        """,
        (
            exchange_id,
            event_type,
            confidence,
            impact_score,
            impact_signal,
            trade_signal,
            priority,
            alpha_score,
            alpha_signal
        )
    )

    conn.commit()

    conn.close()

    return True

