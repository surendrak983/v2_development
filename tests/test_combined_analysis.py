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

from analysis.analysis_engine import (
    AnalysisEngine
)

engine = (
    AnalysisEngine()
)

headline = (
    "Announcement under Regulation 30"
)

pdf_text = """
Company has acquired
74% stake in XYZ Ltd
"""

result = engine.analyze(
    headline,
    pdf_text
)

print(result)