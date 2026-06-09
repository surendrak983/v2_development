class SignalEngine:

    def generate(self, impact):

        score = impact["score"]

        if score >= 90:
            return {
                "signal": "STRONG_BUY",
                "priority": 1
            }

        elif score >= 80:
            return {
                "signal": "BUY_CANDIDATE",
                "priority": 2
            }

        elif score >= 60:
            return {
                "signal": "WATCH",
                "priority": 3
            }

        elif score >= 40:
            return {
                "signal": "LOW_PRIORITY",
                "priority": 4
            }

        return {
            "signal": "IGNORE",
            "priority": 5
        }