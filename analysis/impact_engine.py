class ImpactEngine:

    def score(self, detection):

        event_type = detection["event_type"]

        scores = {

            # Very High Impact

            "buyback": 95,

            "open_offer": 90,

            "order_win": 85,

            "acquisition": 85,

            "merger": 85,

            "promoter_purchase": 80,

            # High Impact

            "bonus": 75,

            "dividend": 70,

            "stock_split": 65,

            "results": 60,

            "fund_raise": 60,

            # Medium Impact

            "rights_issue": 55,

            "preferential_issue": 55,

            "credit_rating": 55,

            # Low Impact

            "board_meeting": 40,

            "investor_meeting": 25,

            # Informational

            "annual_report": 15,

            "postal_ballot": 15,

            "press_release": 10,

            "agm": 10,

            "egm": 10,

            # Default

            "unknown": 0
        }

        score = scores.get(
            event_type,
            0
        )

        if score >= 80:

            signal = "HIGH"

        elif score >= 60:

            signal = "MEDIUM"

        elif score > 0:

            signal = "LOW"

        else:

            signal = "IGNORE"

        return {

            "event_type": event_type,

            "score": score,

            "signal": signal
        }