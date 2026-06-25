class EventDetector:

    def detect(
        self,
        text
    ):

        if not text:

            return {
                "event_type": "unknown",
                "confidence": 0
            }

        text = text.lower()

        # Acquisition

        if (
            "acquisition" in text
            or "acquire" in text
            or "stake acquisition" in text
        ):

            return {
                "event_type": "acquisition",
                "confidence": 95
            }

        # Order Win

        elif (
            "order worth" in text
            or "received order" in text
            or "award of order" in text
            or "receipt of order" in text
        ):

            return {
                "event_type": "order_win",
                "confidence": 95
            }

        # Credit Rating

        elif (
            "credit rating" in text
            or "care ratings" in text
            or "icra" in text
            or "crisil" in text
        ):

            return {
                "event_type": "credit_rating",
                "confidence": 95
            }

        # Dividend

        elif "dividend" in text:

            return {
                "event_type": "dividend",
                "confidence": 90
            }

        # Results

        elif (
            "results" in text
            or "quarter ended" in text
            or "financial results" in text
        ):

            return {
                "event_type": "results",
                "confidence": 90
            }

        # Board Meeting

        elif "board meeting" in text:

            return {
                "event_type": "board_meeting",
                "confidence": 90
            }

        # Investor Meeting

        elif (
            "investor meet" in text
            or "analyst" in text
            or "conference call" in text
        ):

            return {
                "event_type": "investor_meeting",
                "confidence": 90
            }

        # Management Change

        elif "resignation" in text:

            return {
                "event_type": "management_change",
                "confidence": 90
            }

        # Preferential Issue

        elif "preferential issue" in text:

            return {
                "event_type": "preferential_issue",
                "confidence": 95
            }

        # ESOP

        elif (
            "esop" in text
            or "esps" in text
            or "grant of options" in text
        ):

            return {
                "event_type": "esop",
                "confidence": 90
            }

        # Stake Sale

        elif (
            "sale of" in text
            and "equity stake" in text
        ):

            return {
                "event_type": "stake_sale",
                "confidence": 95
            }

        # Credit Facility

        elif "credit facility" in text:

            return {
                "event_type": "fund_raise",
                "confidence": 90
            }

        # Restructuring

        elif "restructuring" in text:

            return {
                "event_type": "restructuring",
                "confidence": 90
            }

        # Allotment

        elif "allotment" in text:

            return {
                "event_type": "allotment",
                "confidence": 90
            }

        # Agreement

        elif (
            "agreement signed" in text
            or "definitive agreement" in text
        ):

            return {
                "event_type": "strategic_agreement",
                "confidence": 95
            }

        return {
            "event_type": "unknown",
            "confidence": 50
        }