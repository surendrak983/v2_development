import fitz


class PDFExtractor:

    def extract_text(self, pdf_path):

        pdf = fitz.open(pdf_path)

        pages = []

        total_chars = 0

        for page in pdf:

            text = page.get_text()

            total_chars += len(text)

            if text:
                pages.append(text)

        page_count = pdf.page_count

        pdf.close()

        return {
            "raw_text": "\n".join(pages),
            "character_count": total_chars,
            "page_count": page_count,
            "is_scanned": total_chars < 500
        }