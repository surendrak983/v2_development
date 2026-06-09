from repository.database import get_connection


class AnnouncementRepository:

    def save(self, row):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
        INSERT OR IGNORE INTO announcements
        (
            exchange_id,
            scrip_code,
            company_name,
            headline,
            category,
            sub_category,
            impact_score,
            announcement_time
        )
        VALUES
        (
            ?,?,?,?,?,?,?,?
        )
        """,
        (
            row["exchange_id"],
            row["scrip_code"],
            row["company_name"],
            row["headline"],
            row["category"],
            row["sub_category"],
            row["impact_score"],
            row["announcement_time"]
        ))

        conn.commit()
        conn.close()