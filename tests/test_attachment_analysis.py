import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from services.attachment_analysis_service import (
    AttachmentAnalysisService
)

service = AttachmentAnalysisService()

result = service.analyze_attachment(
    1
)

print(result)