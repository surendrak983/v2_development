import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from analysis.analysis_engine import (
    AnalysisEngine
)

engine = AnalysisEngine()

samples = [

    "Declaration of Interim Dividend",

    "Disclosure under Regulation 29(2)",

    "Company received order worth Rs 500 crore",

    "Board Meeting to Consider Fund Raising"
]

for text in samples:

    print("\n" + "=" * 60)

    print(text)

    print(
        engine.analyze(text)
    )