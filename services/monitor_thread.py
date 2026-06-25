
import time
from datetime import datetime

from integrations.bse_client import BSEClient
from monitors.announcement_monitor import AnnouncementMonitor
from services.service_state import service_state


def monitor_loop():

    while service_state["monitor"]["running"]:

        try:

            client = BSEClient()

            monitor = AnnouncementMonitor(
                client
            )

            monitor.run()

            service_state[
                "monitor"
            ][
                "last_run"
            ] = datetime.now().strftime(
                "%H:%M:%S"
            )

            service_state[
                "monitor"
            ][
                "records_processed"
            ] += 1

        except Exception as e:

            print(
                f"Monitor Thread Error: {e}"
            )

            service_state[
                "monitor"
            ][
                "error_count"
            ] += 1

        time.sleep(

            service_state[
                "monitor"
            ][
                "interval"
            ]

        )

