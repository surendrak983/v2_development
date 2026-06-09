import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from services.analysis_service import (
    AnalysisService
)

service = AnalysisService()

result = service.analyze_and_store(
    "TEST002",
    "Company received order worth Rs 500 crore"
)

print(result)