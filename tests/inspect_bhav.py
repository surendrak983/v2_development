import sqlite3

conn = sqlite3.connect(
    r"C:\Users\poona\bse_cash_project\Data\market_data.db"
)

cur = conn.cursor()

cur.execute("""
SELECT
    trade_date,
    fininstrm_id,
    symbol,
    isin,
    close_price
FROM bse_cash
LIMIT 20
""")

for row in cur.fetchall():

    print(row)

conn.close()