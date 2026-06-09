import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from pdf.extractor import PDFExtractor
from repository.attachment_repository import (
    AttachmentRepository
)

from pathlib import Path

pdf_folder = Path(
    r"C:\Users\poona\v2_development\data\attachments\500325"
)

pdf_files = list(pdf_folder.glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError(
        f"No PDF files found in {pdf_folder}"
    )

pdf_file = str(pdf_files[0])

print(f"Using PDF: {pdf_file}")

extractor = PDFExtractor()

result = extractor.extract_text(pdf_file)

repo = AttachmentRepository()

repo.save({
    "scrip_code": "500325",
    "pdf_file": pdf_file,
    "page_count": result["page_count"],
    "character_count": result["character_count"],
    "is_scanned": int(result["is_scanned"]),
    "raw_text": result["raw_text"]
})

print("Saved successfully")