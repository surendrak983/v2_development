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

from services.attachment_processor import (
    AttachmentProcessor
)

processor = (
    AttachmentProcessor()
)

result = processor.process(
    "540879",
    "test.pdf"
)

print(result)