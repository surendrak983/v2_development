import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from pdf.extractor import PDFExtractor

pdf_file = (
    r"C:\Users\poona\v2_development\data\attachments"
    r"\61e3d63d-9774-4cd8-b2e3-4f63c35d54bb_61E3D63D_9774_4CD8_B2E3_4F63C35D54BB_102446.pdf"
)

extractor = PDFExtractor()

text = extractor.extract_text(pdf_file)

print("=" * 80)
print(text[:5000])
print("=" * 80)
print(f"Characters extracted: {len(text)}")