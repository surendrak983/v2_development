import sys
from pathlib import Path

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from services.attachment_download_service import (
    AttachmentDownloadService
)

service = (
    AttachmentDownloadService()
)

pdf = service.download_pdf(
    "540879",
    "12b079fd-9a0e-43d5-b8f2-f30ea898b3b4.pdf"
)

print(pdf)