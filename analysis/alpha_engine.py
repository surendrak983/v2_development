
class AlphaEngine:

    def calculate(
        self,
        impact_score,
        confidence,
        priority
    ):

        alpha_score = impact_score

        # -------------------------
        # Confidence bonus
        # -------------------------

        if confidence >= 90:

            alpha_score += 5

        elif confidence >= 75:

            alpha_score += 2

        # -------------------------
        # Priority bonus
        # -------------------------

        if priority == 1:

            alpha_score += 5

        elif priority == 2:

            alpha_score += 2

        # -------------------------
        # Cap score
        # -------------------------

        alpha_score = max(
            0,
            min(
                alpha_score,
                100
            )
        )

        # -------------------------
        # Alpha Signal
        # -------------------------

        if alpha_score >= 90:

            alpha_signal = "STRONG_BUY"

        elif alpha_score >= 75:

            alpha_signal = "BUY"

        elif alpha_score >= 60:

            alpha_signal = "WATCH"

        else:

            alpha_signal = "IGNORE"

        return {

            "alpha_score": alpha_score,

            "alpha_signal": alpha_signal

        }

