# count_analysis.py

from repository.database import get_connection

conn = get_connection()

cur = conn.cursor()

cur.execute(
    "SELECT COUNT(*) FROM analysis_results"
)

print(cur.fetchone()[0])

conn.close()