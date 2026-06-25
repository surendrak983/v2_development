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

REPORT_DIR = PROJECT_ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)

# ----------------------------
# Database
# ----------------------------

DB_PATH = DATA_DIR / "bse_monitor.db"

MARKET_DATA_DB_PATH = (
    Path(
         r"C:\Users\poona\.claude\bse_cash_project_work\bse_cash_project\Data\bse_cash_eod.db"
    )
)

NSE_TECH_PROJECT_ROOT = (
    Path(
        r"C:\Users\poona\A_tech_indicator"
    )
)

NSE_CASH_DIR = NSE_TECH_PROJECT_ROOT / "Data" / "Cash"
NSE_FUTURES_DIR = NSE_TECH_PROJECT_ROOT / "Data" / "Futures"
NSE_OPTIONS_DIR = NSE_TECH_PROJECT_ROOT / "Data" / "Options"
NSE_CHARTS_DIR = NSE_TECH_PROJECT_ROOT / "Charts"

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
