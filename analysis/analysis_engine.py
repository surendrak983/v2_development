from analysis.event_detector import EventDetector
from analysis.impact_engine import ImpactEngine
from analysis.signal_engine import SignalEngine


class AnalysisEngine:

    def __init__(self):

        self.detector = EventDetector()

        self.impact_engine = ImpactEngine()

        self.signal_engine = SignalEngine()

    def analyze(self, text):

        detection = self.detector.detect(text)

        impact = self.impact_engine.score(
            detection
        )

        signal = self.signal_engine.generate(
            impact
        )

        return {

            "event_type":
                detection["event_type"],

            "confidence":
                detection["confidence"],

            "impact_score":
                impact["score"],

            "impact_signal":
                impact["signal"],

            "trade_signal":
                signal["signal"],

            "priority":
                signal["priority"]
        }