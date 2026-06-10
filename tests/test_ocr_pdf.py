import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

PDF_PATH = r"test.pdf"

POPPLER_PATH = (
    r"C:\poppler\poppler-26.02.0\Library\bin"
)

pages = convert_from_path(
    PDF_PATH,
    poppler_path=POPPLER_PATH
)

full_text = ""

for i, page in enumerate(pages):

    print(f"Processing page {i+1}")

    text = pytesseract.image_to_string(
        page
    )

    full_text += text

print("\n")
print("=" * 80)
print("OCR OUTPUT")
print("=" * 80)

print(full_text[:10000])