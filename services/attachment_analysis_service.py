from analysis.analysis_engine import (
    AnalysisEngine
)

from repository.attachment_repository import (
    AttachmentRepository
)


class AttachmentAnalysisService:

    def __init__(self):

        self.repo = AttachmentRepository()

        self.engine = AnalysisEngine()

    def analyze_attachment(
        self,
        attachment_id
    ):

        text = self.repo.get_text_by_id(
            attachment_id
        )

        if not text:

            return None

        return self.engine.analyze(
            text
        )