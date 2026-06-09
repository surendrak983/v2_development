import sqlite3

from core.config import DB_PATH


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():

    conn = get_connection()

    cur = conn.cursor()

    # ----------------------------------
    # Announcements table
    # ----------------------------------

    cur.execute("""
    CREATE TABLE IF NOT EXISTS announcements
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        exchange_id TEXT UNIQUE,

        scrip_code TEXT,
        company_name TEXT,

        headline TEXT,
        category TEXT,
        sub_category TEXT,

        impact_score INTEGER,

        announcement_time TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ----------------------------------
    # Attachment text table
    # ----------------------------------

    cur.execute("""
    CREATE TABLE IF NOT EXISTS attachment_texts
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        scrip_code TEXT,

        pdf_file TEXT,

        page_count INTEGER,

        character_count INTEGER,

        is_scanned INTEGER,

        raw_text TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    conn.close()