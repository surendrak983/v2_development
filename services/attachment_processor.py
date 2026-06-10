from services.pdf_text_extractor import (
    PDFTextExtractor
)

from repository.attachment_text_repository import (
    save_attachment_text
)


class AttachmentProcessor:

    def __init__(self):

        self.extractor = (
            PDFTextExtractor()
        )

    def process(
        self,
        scrip_code,
        pdf_path
    ):

        result = (
            self.extractor
            .extract_text_with_metadata(
                pdf_path
            )
        )

        save_attachment_text(
            scrip_code=scrip_code,
            pdf_file=pdf_path,
            page_count=result[
                "page_count"
            ],
            character_count=len(
                result["text"]
            ),
            is_scanned=result[
                "is_scanned"
            ],
            raw_text=result[
                "text"
            ]
        )

        return result