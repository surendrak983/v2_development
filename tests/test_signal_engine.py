import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from analysis.event_detector import EventDetector
from analysis.impact_engine import ImpactEngine
from analysis.signal_engine import SignalEngine

detector = EventDetector()
impact_engine = ImpactEngine()
signal_engine = SignalEngine()

samples = [
    "Declaration of Interim Dividend",
    "Disclosure under Regulation 29(2)",
    "Company received order worth Rs 500 crore",
    "Board Meeting to Consider Fund Raising"
]

for text in samples:

    detection = detector.detect(text)

    impact = impact_engine.score(detection)

    signal = signal_engine.generate(impact)

    print("\n" + "=" * 60)
    print(text)
    print(detection)
    print(impact)
    print(signal)