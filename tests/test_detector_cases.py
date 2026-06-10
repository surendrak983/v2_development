import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from analysis.event_detector import (
    EventDetector
)

detector = EventDetector()

samples = [

    "Disclosure under Regulation 7(2) of SEBI (PIT) Regulations, 2015",

    "Analyst / Investor Meet",

    "Press Release",

    "Annual Report",

    "Postal Ballot",

    "Rights Issue",

    "Credit Rating"
]

for text in samples:

    print()
    print("=" * 60)

    print(text)

    print(
        detector.detect(text)
    )