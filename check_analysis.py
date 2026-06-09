from repository.database import get_connection

conn = get_connection()

cur = conn.cursor()

cur.execute("""
SELECT *
FROM analysis_results
""")

for row in cur.fetchall():
    print(row)

conn.close()