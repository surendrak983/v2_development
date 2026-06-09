from repository.database import (
    initialize_database
)

from integrations.bse_client import (
    BSEClient
)

from monitors.announcement_monitor import (
    AnnouncementMonitor
)


def startup():

    initialize_database()

    client = BSEClient()

    monitor = AnnouncementMonitor(
        client
    )

    monitor.run()

    print("BSE V2 Started")


if __name__ == "__main__":
    startup()