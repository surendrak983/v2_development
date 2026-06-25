import sqlite3

SOURCE_DB = (
    r"C:\Users\poona\.claude\bse_cash_project_work"
    r"\bse_cash_project\Data\bse_cash_eod.db"
)

TARGET_DB = r"data\market_engine.db"


source_conn = sqlite3.connect(SOURCE_DB)
target_conn = sqlite3.connect(TARGET_DB)

source_cur = source_conn.cursor()
target_cur = target_conn.cursor()

print("Reading source data...")

source_cur.execute(
    """
    SELECT *
    FROM bse_cash_eod
    """
)

rows = source_cur.fetchall()

print(f"Rows found: {len(rows):,}")

target_cur.executemany(
    """
    INSERT OR REPLACE INTO bse_cash_eod
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    rows
)

target_conn.commit()

print("Migration complete")

source_conn.close()
target_conn.close()