from analysis.analysis_engine import (
    AnalysisEngine
)

from repository.analysis_repository import (
    save_analysis
)


class AnalysisService:

    def __init__(self):

        self.engine = AnalysisEngine()

    def analyze_announcement(
        self,
        headline
    ):

        return self.engine.analyze(
            headline
        )

    def analyze_and_store(
        self,
        exchange_id,
        headline
    ):

        result = self.engine.analyze(
            headline
        )

        save_analysis(
            exchange_id=exchange_id,
            event_type=result["event_type"],
            confidence=result["confidence"],
            impact_score=result["impact_score"],
            impact_signal=result["impact_signal"],
            trade_signal=result["trade_signal"],
            priority=result["priority"]
        )

        return result