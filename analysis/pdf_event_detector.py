class PDFEventDetector:

    def detect(
        self,
        text
    ):

        text = text.lower()

        if (
            "investor presentation" in text
            or "analyst / institutional investor meeting" in text
            or "investor meet" in text
        ):

            return {
                "event_type": "investor_meeting",
                "confidence": 95
            }

        if (
            "acquired" in text
            or "acquisition" in text
            or "stake in" in text
        ):

            return {
                "event_type": "acquisition",
                "confidence": 95
            }

        if (
            "order worth" in text
            or "received order" in text
            or "contract worth" in text
            or "purchase order" in text
        ):

            return {
                "event_type": "order_win",
                "confidence": 95
            }

        if (
            "buyback" in text
            or "buy-back" in text
        ):

            return {
                "event_type": "buyback",
                "confidence": 95
            }

        if (
            "rights issue" in text
        ):

            return {
                "event_type": "rights_issue",
                "confidence": 95
            }

        if (
            "credit rating" in text
            or "rating reaffirmed" in text
            or "care ratings" in text
            or "icra" in text
            or "crisil" in text
        ):

            return {
                "event_type": "credit_rating",
                "confidence": 95
            }

        if (
            "dividend" in text
        ):

            return {
                "event_type": "dividend",
                "confidence": 95
            }

        if (
            "financial results" in text
            or "quarter ended" in text
            or "standalone and consolidated results" in text
        ):

            return {
                "event_type": "results",
                "confidence": 95
            }

        return {
            "event_type": "unknown",
            "confidence": 0
        }