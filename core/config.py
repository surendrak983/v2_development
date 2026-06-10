from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ----------------------------
# Data folders
# ----------------------------

DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

ATTACHMENT_DIR = DATA_DIR / "attachments"
ATTACHMENT_DIR.mkdir(exist_ok=True)

LOG_DIR = DATA_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# ----------------------------
# Database
# ----------------------------

DB_PATH = DATA_DIR / "bse_monitor.db"

MARKET_DATA_DB_PATH = (
    Path(
        r"C:\Users\poona\bse_cash_project\Data\market_data.db"
    )
)

SEEN_FILE = DATA_DIR / "seen.json"

# ----------------------------
# Filters
# ----------------------------

MIN_PRICE_FILTER = 50
MIN_VOLUME_FILTER = 100000

# ----------------------------
# Polling
# ----------------------------

POLL_INTERVAL_SECONDS = 60

# ----------------------------
# Integrations
# ----------------------------

TELEGRAM_ENABLED = True