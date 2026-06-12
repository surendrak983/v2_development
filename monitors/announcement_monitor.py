from repository.announcement_repository import (
    AnnouncementRepository
)

from services.analysis_service import (
    AnalysisService
)

from services.attachment_download_service import (
    AttachmentDownloadService
)

from services.attachment_processor import (
    AttachmentProcessor
)

from core.notifier import (
    info
)


class AnnouncementMonitor:

    def __init__(self, client):

        self.client = client

        self.repo = AnnouncementRepository()

        self.analysis_service = AnalysisService()

        self.download_service = AttachmentDownloadService()

        self.attachment_processor = AttachmentProcessor()

    def run(self):

        announcements = self.client.get_announcements()

        info(
            f"Fetched {len(announcements)} announcements"
        )

        for item in announcements:

            row = {
                "exchange_id": item["exchange_id"],
                "scrip_code": item["scrip_code"],
                "company_name": item["company_name"],
                "headline": item["headline"],
                "category": "UNKNOWN",
                "sub_category": "UNKNOWN",
                "impact_score": 0,
                "announcement_time": item["announcement_time"],
            }

            is_new = self.repo.save(row)

            if not is_new:
                continue

            pdf_text = None

            attachment_name = item.get(
                "attachment_name",
                ""
            )

            if attachment_name:

                try:

                    pdf_path = (
                        self.download_service
                        .download_pdf(
                            item["scrip_code"],
                            attachment_name
                        )
                    )

                    if pdf_path:

                        result = (
                            self.attachment_processor
                            .process(
                                item["scrip_code"],
                                pdf_path
                            )
                        )

                        pdf_text = result["text"]

                except Exception as e:

                    print(
                        f"PDF Error: {e}"
                    )

            analysis = (
                self.analysis_service
                .analyze_and_store(
                    exchange_id=item["exchange_id"],
                    headline=item.get(
                        "analysis_text",
                        item["headline"]
                    ),
                    pdf_text=pdf_text
                )
            )

            info(
                f"{item['company_name']} | "
                f"{analysis['event_type']} | "
                f"{analysis['trade_signal']}"
            )
