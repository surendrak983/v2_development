import time
from datetime import datetime

from services.service_state import service_state


def monitor_loop():

    while service_state["monitor"]["running"]:

        try:

            print(
                "[MONITOR]",
                datetime.now()
            )

            service_state["monitor"]["last_run"] = datetime.now()

            service_state["monitor"]["records_processed"] += 1

        except Exception:

            service_state["monitor"]["error_count"] += 1

        time.sleep(
            service_state["monitor"]["interval"]
        )