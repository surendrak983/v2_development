from repository.database import get_connection


def save_analysis(
    exchange_id,
    event_type,
    confidence,
    impact_score,
    impact_signal,
    trade_signal,
    priority
):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
    INSERT INTO analysis_results
    (
        exchange_id,
        event_type,
        confidence,
        impact_score,
        impact_signal,
        trade_signal,
        priority
    )
    VALUES
    (
        ?, ?, ?, ?, ?, ?, ?
    )
    """, (
        exchange_id,
        event_type,
        confidence,
        impact_score,
        impact_signal,
        trade_signal,
        priority
    ))

    conn.commit()

    conn.close()