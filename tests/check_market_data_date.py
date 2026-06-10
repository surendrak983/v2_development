import sqlite3

conn = sqlite3.connect(
    r"C:\Users\poona\bse_cash_project\Data\market_data.db"
)

cur = conn.cursor()

cur.execute("""
SELECT MAX(trade_date)
FROM bse_cash
""")

row = cur.fetchone()

print(
    "Latest Bhav Date:",
    row[0]
)

conn.close()