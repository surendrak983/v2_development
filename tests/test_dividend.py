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

engine = AnalysisEngine()

result = engine.analyze(
    headline=
"""
Interim dividend of Rs.12 per share
"""
)

print(
    result
)