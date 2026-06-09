import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from analysis.event_detector import EventDetector

detector = EventDetector()

samples = [

    "Board Meeting to Consider Fund Raising",

    "Declaration of Interim Dividend",

    "Disclosure under Regulation 29(2)",

    "Company received order worth Rs 500 crore"
]

for text in samples:

    result = detector.detect(text)

    print()
    print(text)
    print(result)