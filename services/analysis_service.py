from analysis.analysis_engine import (
    AnalysisEngine
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