class PriorityEngine:

    PRIORITY_MAP = {

        # Highest priority
        "order_win": 1,
        "promoter_purchase": 1,
        "acquisition": 1,

        # Medium
        "fund_raise": 2,

        # Lower
        "dividend": 3,

        # Lowest
        "board_meeting": 4
    }

    def get_priority(self, event_type: str) -> int:

        return self.PRIORITY_MAP.get(
            event_type,
            4
        )