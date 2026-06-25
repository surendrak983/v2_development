
from analysis.event_detector import EventDetector
from analysis.pdf_event_detector import PDFEventDetector
from analysis.entity_extractor import EntityExtractor
from analysis.impact_engine import ImpactEngine
from analysis.signal_engine import SignalEngine
from analysis.adaptive_scoring_engine import AdaptiveScoringEngine
from analysis.alpha_engine import AlphaEngine


class AnalysisEngine:

    def __init__(self):

        self.detector = EventDetector()

        self.pdf_detector = PDFEventDetector()

        self.entity_extractor = EntityExtractor()

        self.impact_engine = ImpactEngine()

        self.signal_engine = SignalEngine()

        self.adaptive_engine = AdaptiveScoringEngine()

        self.alpha_engine = AlphaEngine()

    def analyze(
        self,
        headline,
        pdf_text=None
    ):

        full_text = headline or ""

        if pdf_text and len(pdf_text.strip()) > 0:
            full_text += "\n\n" + pdf_text

        # Event Detection
        detection = self.detector.detect(full_text)

        if detection["event_type"] == "unknown" and pdf_text:

            pdf_detection = self.pdf_detector.detect(
                pdf_text
            )

            if pdf_detection["event_type"] != "unknown":
                detection = pdf_detection

        # Entity Extraction
        entities = self.entity_extractor.extract(
            full_text
        )

        analysis_result = {}

        analysis_result.update(detection)

        analysis_result.update(entities)

        # Impact Engine
        impact = self.impact_engine.score(
            analysis_result
        )

        # Adaptive Layer
        adjustment = self.adaptive_engine.get_adjustment(
            detection["event_type"]
        )

        impact["score"] += adjustment

        impact["score"] = max(
            0,
            min(100, impact["score"])
        )

        if impact["score"] >= 90:
            impact["signal"] = "VERY_HIGH"

        elif impact["score"] >= 80:
            impact["signal"] = "HIGH"

        elif impact["score"] >= 65:
            impact["signal"] = "MEDIUM"

        else:
            impact["signal"] = "LOW"

        # Signal Engine
        signal = self.signal_engine.generate(
            impact
        )

        # Alpha Engine
        alpha = self.alpha_engine.calculate(
            impact["score"],
            detection["confidence"],
            signal["priority"]
        )

        result = {

            "event_type": detection["event_type"],

            "confidence": detection["confidence"],

            "impact_score": impact["score"],

            "impact_signal": impact["signal"],

            "trade_signal": signal["signal"],

            "priority": signal["priority"],

            "alpha_score": alpha["alpha_score"],

            "alpha_signal": alpha["alpha_signal"]

        }

        result.update(
            entities
        )

        return result

