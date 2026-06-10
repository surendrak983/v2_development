from analysis.event_detector import (
    EventDetector
)

from analysis.pdf_event_detector import (
    PDFEventDetector
)

from analysis.impact_engine import (
    ImpactEngine
)

from analysis.signal_engine import (
    SignalEngine
)


class AnalysisEngine:

    def __init__(self):

        self.detector = (
            EventDetector()
        )

        self.pdf_detector = (
            PDFEventDetector()
        )

        self.impact_engine = (
            ImpactEngine()
        )

        self.signal_engine = (
            SignalEngine()
        )

    def analyze(
        self,
        headline,
        pdf_text=None
    ):

        detection = (
            self.detector.detect(
                headline
            )
        )

        if (
            detection["event_type"]
            == "unknown"
            and pdf_text
            and len(
                pdf_text.strip()
            ) > 0
        ):

            pdf_detection = (
                self.pdf_detector.detect(
                    pdf_text
                )
            )

            if (
                pdf_detection["event_type"]
                != "unknown"
            ):

                detection = (
                    pdf_detection
                )

        impact = (
            self.impact_engine.score(
                detection
            )
        )

        signal = (
            self.signal_engine.generate(
                impact
            )
        )

        return {

            "event_type":
                detection[
                    "event_type"
                ],

            "confidence":
                detection[
                    "confidence"
                ],

            "impact_score":
                impact[
                    "score"
                ],

            "impact_signal":
                impact[
                    "signal"
                ],

            "trade_signal":
                signal[
                    "signal"
                ],

            "priority":
                signal[
                    "priority"
                ]
        }