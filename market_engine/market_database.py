from pathlib import Path
import sqlite3


DB_PATH = (
    Path(__file__).parent.parent
    / "data"
    / "market_engine.db"
)


CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS bse_cash_eod (

    trade_date TEXT NOT NULL,

    fininstrm_id INTEGER NOT NULL,

    symbol TEXT,

    isin TEXT,

    open_price REAL,

    high_price REAL,

    low_price REAL,

    close_price REAL,

    last_price REAL,

    prev_close REAL,

    volume INTEGER,

    turnover REAL,

    trades INTEGER,

    downloaded_at TEXT NOT NULL,

    PRIMARY KEY (
        trade_date,
        fininstrm_id
    )
)
"""


def get_connection():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    return conn


def initialize_database():

    with get_connection() as conn:

        conn.execute(CREATE_TABLE_SQL)

        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_symbol

            ON bse_cash_eod(symbol)
            """
        )

        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_trade_date

            ON bse_cash_eod(trade_date)
            """
        )