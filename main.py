import time
from datetime import datetime

from repository.database import (
    initialize_database
)

from integrations.bse_client import (
    BSEClient
)

from monitors.announcement_monitor import (
    AnnouncementMonitor
)

from core.config import (
    POLL_INTERVAL_SECONDS
)
from repository.stock_repository import StockRepository
from repository.company_repository import CompanyRepository

StockRepository.load()
CompanyRepository.load()

def startup():

    initialize_database()

    client = BSEClient()

    monitor = AnnouncementMonitor(
        client
    )

    print("=" * 60)
    print("BSE V2 Started")
    print(
        f"Polling every "
        f"{POLL_INTERVAL_SECONDS} seconds"
    )
    print("=" * 60)

    while True:

        try:

            print()
            print(
                f"[{datetime.now()}] "
                f"Checking announcements..."
            )

            monitor.run()

        except Exception as e:

            print(
                f"ERROR: {e}"
            )

        time.sleep(
            POLL_INTERVAL_SECONDS
        )


if __name__ == "__main__":

    try:

        startup()

    except KeyboardInterrupt:

        print()
        print(
            "BSE V2 stopped by user"
        )