from repository.database import get_connection


def save_analysis(
    newsid,
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
    INSERT INTO analysis_results(
        newsid,
        event_type,
        confidence,
        impact_score,
        impact_signal,
        trade_signal,
        priority
    )
    VALUES(
        ?,?,?,?,?,?,?
    )
    """, (
        newsid,
        event_type,
        confidence,
        impact_score,
        impact_signal,
        trade_signal,
        priority
    ))

    conn.commit()

    conn.close()