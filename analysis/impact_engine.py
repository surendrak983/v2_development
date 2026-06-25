
from analysis.adaptive_scoring_engine import (
    AdaptiveScoringEngine
)


class ImpactEngine:

    def __init__(self):

        self.adaptive_engine = (
            AdaptiveScoringEngine()
        )

    def score(
        self,
        analysis
    ):

        event_type = (
            analysis.get(
                "event_type",
                "unknown"
            )
        )

        score = 50

        # -------------------------
        # Acquisition
        # -------------------------

        if event_type == "acquisition":

            score = 85

            stake = analysis.get(
                "stake_percent"
            )

            if stake:

                if stake >= 50:

                    score += 10

                elif stake >= 25:

                    score += 5

        # -------------------------
        # Order Win
        # -------------------------

        elif event_type == "order_win":

            score = 80

            amount = analysis.get(
                "amount_crore"
            )

            if amount:

                if amount >= 1000:

                    score += 15

                elif amount >= 500:

                    score += 10

                elif amount >= 100:

                    score += 5

        # -------------------------
        # Dividend
        # -------------------------

        elif event_type == "dividend":

            score = 80

            dividend = analysis.get(
                "dividend"
            )

            if dividend:

                if dividend >= 10:

                    score += 10

                elif dividend >= 5:

                    score += 5

        # -------------------------
        # Credit Rating
        # -------------------------

        elif event_type == "credit_rating":

            score = 80

            rating = analysis.get(
                "rating"
            )

            if rating == "AAA":

                score += 10

            elif rating == "AA+":

                score += 5

        # -------------------------
        # Results
        # -------------------------

        elif event_type == "results":

            score = 75

        # -------------------------
        # Buyback
        # -------------------------

        elif event_type == "buyback":

            score = 95

        # -------------------------
        # Management Change
        # -------------------------

        elif event_type == "management_change":

            score = 60

        # -------------------------
        # Board Meeting
        # -------------------------

        elif event_type == "board_meeting":

            score = 55

        # -------------------------
        # Investor Meeting
        # -------------------------

        elif event_type == "investor_meeting":

            score = 50

        # -------------------------
        # Unknown
        # -------------------------

        else:

            score = 50

        # -------------------------
        # Adaptive Scoring
        # -------------------------

        adjustment = (
            self.adaptive_engine
            .get_adjustment(
                event_type
            )
        )

        score += adjustment

        # Keep score in range

        score = max(
            0,
            min(
                score,
                100
            )
        )

        # -------------------------
        # Impact Signal
        # -------------------------

        if score >= 90:

            impact_signal = "VERY_HIGH"

        elif score >= 80:

            impact_signal = "HIGH"

        elif score >= 65:

            impact_signal = "MEDIUM"

        else:

            impact_signal = "LOW"

        return {

            "score":
                score,

            "signal":
                impact_signal
        }
