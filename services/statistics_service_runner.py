from datetime import datetime

from services.service_state import service_state


def run_statistics():

    service_state["statistics"]["last_run"] = datetime.now()

    service_state["statistics"]["records_processed"] += 1