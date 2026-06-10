from repository.database import get_connection


class AttachmentRepository:

    def save(self, data):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
        INSERT INTO attachment_texts
        (
            scrip_code,
            pdf_file,
            page_count,
            character_count,
            is_scanned,
            raw_text
        )
        VALUES
        (
            ?,?,?,?,?,?
        )
        """,
        (
            data["scrip_code"],
            data["pdf_file"],
            data["page_count"],
            data["character_count"],
            data["is_scanned"],
            data["raw_text"]
        ))

        conn.commit()

        conn.close()

    def get_latest(self, limit=10):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
        SELECT
            id,
            scrip_code,
            pdf_file,
            character_count,
            is_scanned
        FROM attachment_texts
        ORDER BY id DESC
        LIMIT ?
        """, (limit,))

        rows = cur.fetchall()

        conn.close()

        return rows

    def get_text_by_id(
        self,
        attachment_id
    ):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
        SELECT
            raw_text
        FROM attachment_texts
        WHERE id = ?
        """, (
            attachment_id,
        ))

        row = cur.fetchone()

        conn.close()

        if not row:

            return None

        return row[0]