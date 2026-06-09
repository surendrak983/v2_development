from pathlib import Path

from core.config import ATTACHMENT_DIR


class AttachmentService:

    def get_company_folder(
        self,
        scrip_code
    ):

        folder = (
            ATTACHMENT_DIR /
            str(scrip_code)
        )

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return folder