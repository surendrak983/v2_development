import fitz

pdf_file = r"C:\Users\poona\v2_development\data\attachments\61e3d63d-9774-4cd8-b2e3-4f63c35d54bb_61E3D63D_9774_4CD8_B2E3_4F63C35D54BB_102446.pdf"

pdf = fitz.open(pdf_file)

print(f"Pages: {pdf.page_count}")

for i in range(pdf.page_count):

    page = pdf[i]

    text = page.get_text()

    images = page.get_images()

    print(
        f"Page {i+1}: "
        f"text={len(text)} "
        f"images={len(images)}"
    )

pdf.close()