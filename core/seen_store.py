import json

from core.config import SEEN_FILE


def load_seen():

    if not SEEN_FILE.exists():
        return {
            "announcements": [],
            "results": []
        }

    try:
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        return {
            "announcements": [],
            "results": []
        }


def save_seen(data):

    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)