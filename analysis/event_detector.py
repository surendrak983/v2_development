class EventDetector:

    def detect(self, text):

        text = text.lower()

        rules = [

            ("dividend", [
                "dividend",
                "interim dividend",
                "final dividend"
            ]),

            ("buyback", [
                "buyback",
                "buy-back"
            ]),

            ("bonus", [
                "bonus issue",
                "issue of bonus shares"
            ]),

            ("stock_split", [
                "stock split",
                "split of equity shares",
                "sub-division"
            ]),

            ("board_meeting", [
                "board meeting"
            ]),

            ("results", [
                "financial results",
                "quarterly results",
                "audited results",
                "unaudited results"
            ]),

            ("order_win", [
                "order received",
                "received order",
                "work order",
                "letter of award",
                "contract awarded",
                "order worth",
                "contract worth",
                "purchase order"
            ]),

            ("promoter_purchase", [
                "regulation 29(2)",
                "acquisition of shares",
                "promoter acquired"
            ])
        ]

        for event_type, keywords in rules:

            for keyword in keywords:

                if keyword in text:

                    return {
                        "event_type": event_type,
                        "confidence": 90
                    }

        return {
            "event_type": "unknown",
            "confidence": 0
        }