from datetime import datetime
from zoneinfo import ZoneInfo


def utc_to_ist(timestamp):

    if not timestamp:
        return ""

    try:

        dt = datetime.fromisoformat(
            str(timestamp)
        )

        dt = dt.replace(
            tzinfo=ZoneInfo("UTC")
        )

        dt = dt.astimezone(
            ZoneInfo("Asia/Kolkata")
        )

        return dt.strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    except Exception:

        return str(timestamp)