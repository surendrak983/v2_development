class ImpactEngine:

    def score(self, detection):

        event_type = detection["event_type"]

        scores = {

            "buyback": 95,

            "order_win": 85,

            "promoter_purchase": 80,

            "dividend": 70,

            "bonus": 75,

            "stock_split": 65,

            "board_meeting": 40,

            "results": 60,

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