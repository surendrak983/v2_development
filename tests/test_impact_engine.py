import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from analysis.event_detector import EventDetector
from analysis.impact_engine import ImpactEngine

detector = EventDetector()

engine = ImpactEngine()

samples = [

    "Declaration of Interim Dividend",

    "Disclosure under Regulation 29(2)",

    "Company received order worth Rs 500 crore",

    "Board Meeting to Consider Fund Raising"
]

for text in samples:

    detection = detector.detect(text)

    impact = engine.score(detection)

    print()
    print(text)

    print(detection)

    print(impact)