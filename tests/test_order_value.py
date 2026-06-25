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

text = """
Company has received order worth Rs. 2480 crore
from Ministry of Defence.
"""

result = engine.analyze(
    headline=text
)

print(result)