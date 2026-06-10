from pathlib import Path

from tempfile import gettempdir

from bse import BSE


class AttachmentDownloadService:

    def __init__(self):

        self.base_folder = Path(
            "data/attachments"
        )

        self.base_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    def download_pdf(
        self,
        scrip_code,
        attachment_name
    ):

        if not attachment_name:

            return None

        company_folder = (
            self.base_folder
            / str(scrip_code)
        )

        company_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        pdf_path = (
            company_folder
            / attachment_name
        )

        if pdf_path.exists():

            return str(pdf_path)

        url = (
            "https://www.bseindia.com/"
            "xml-data/corpfiling/"
            "AttachLive/"
            + attachment_name
        )

        try:

            with BSE(gettempdir()) as bse:

                response = (
                    bse.session.get(
                        url,
                        timeout=30
                    )
                )

                if (
                    response.status_code
                    == 200
                ):

                    with open(
                        pdf_path,
                        "wb"
                    ) as f:

                        f.write(
                            response.content
                        )

                    return str(
                        pdf_path
                    )

        except Exception as e:

            print(
                f"PDF Download Error: {e}"
            )

        return None