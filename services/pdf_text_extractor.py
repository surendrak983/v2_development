import pdfplumber
import pytesseract

from pdf2image import convert_from_path


class PDFTextExtractor:

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

        self.poppler_path = (
            r"C:\poppler\poppler-26.02.0\Library\bin"
        )

    def extract_text(
        self,
        pdf_path
    ):

        result = self.extract_text_with_metadata(
            pdf_path
        )

        return result["text"]

    def extract_text_with_metadata(
        self,
        pdf_path
    ):

        text = ""

        page_count = 0

        try:

            with pdfplumber.open(
                pdf_path
            ) as pdf:

                page_count = len(
                    pdf.pages
                )

                for page in pdf.pages:

                    page_text = (
                        page.extract_text()
                    )

                    if page_text:

                        text += (
                            page_text
                            + "\n"
                        )

            if len(
                text.strip()
            ) > 100:

                return {

                    "text":
                        text,

                    "page_count":
                        page_count,

                    "character_count":
                        len(text),

                    "is_scanned":
                        0
                }

        except Exception as e:

            print(
                f"PDF extraction error: {e}"
            )

        text = self._extract_with_ocr(
            pdf_path
        )

        pages = convert_from_path(
            pdf_path,
            poppler_path=self.poppler_path
        )

        return {

            "text":
                text,

            "page_count":
                len(pages),

            "character_count":
                len(text),

            "is_scanned":
                1
        }

    def _extract_with_ocr(
        self,
        pdf_path
    ):

        text = ""

        pages = convert_from_path(
            pdf_path,
            poppler_path=self.poppler_path
        )

        for page in pages:

            page_text = (
                pytesseract
                .image_to_string(
                    page
                )
            )

            text += (
                page_text
                + "\n"
            )

        return text