from repository.announcement_repository import (
    AnnouncementRepository
)

from services.analysis_service import (
    AnalysisService
)

from core.notifier import info


class AnnouncementMonitor:

    def __init__(self, client):

        self.client = client

        self.repo = AnnouncementRepository()

        self.analysis_service = AnalysisService()

    def run(self):

        announcements = (
            self.client.get_announcements()
        )

        info(
            f"Fetched {len(announcements)} announcements"
        )

        for item in announcements:

            row = {

                "exchange_id":
                    item["exchange_id"],

                "scrip_code":
                    item["scrip_code"],

                "company_name":
                    item["company_name"],

                "headline":
                    item["headline"],

                "category":
                    "UNKNOWN",

                "sub_category":
                    "UNKNOWN",

                "impact_score":
                    0,

                "announcement_time":
                    item["announcement_time"]
            }

            self.repo.save(row)

            analysis = (
                self.analysis_service
                .analyze_and_store(
                    item["exchange_id"],
                    item.get(
                        "analysis_text",
                        item["headline"]
                    )
                )
            )

            info(
                f"{item['company_name']} | "
                f"{analysis['event_type']} | "
                f"{analysis['trade_signal']}"
            )