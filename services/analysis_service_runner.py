from datetime import datetime

from services.service_state import service_state


def run_analysis():

    service_state["analysis"]["last_run"] = datetime.now()

    service_state["analysis"]["records_processed"] += 1