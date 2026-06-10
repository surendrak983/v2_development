from repository.database import (
    get_connection
)


def save_attachment_text(
    scrip_code,
    pdf_file,
    page_count,
    character_count,
    is_scanned,
    raw_text
):

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
        ?, ?, ?, ?, ?, ?
    )
    """, (
        scrip_code,
        pdf_file,
        page_count,
        character_count,
        is_scanned,
        raw_text
    ))

    conn.commit()

    conn.close()