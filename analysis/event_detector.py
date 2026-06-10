class EventDetector:

    def detect(self, text):

        text = text.lower()

        rules = [

            # Highest priority events

            ("buyback", [
                "buyback",
                "buy-back"
            ]),

            ("open_offer", [
                "open offer"
            ]),

            ("acquisition", [
                "acquisition",
                "acquire",
                "acquired stake",
                "strategic acquisition"
            ]),

            ("merger", [
                "merger",
                "amalgamation",
                "scheme of arrangement"
            ]),

            # Corporate actions

            ("dividend", [
                "dividend",
                "interim dividend",
                "final dividend"
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

            ("rights_issue", [
                "rights issue",
                "rights entitlement"
            ]),

            ("preferential_issue", [
                "preferential issue",
                "preferential allotment"
            ]),

            # Fund raising

            ("fund_raise", [
                "fund raising",
                "raise funds",
                "raising funds",
                "qip",
                "qualified institutions placement"
            ]),

            # Business developments

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

            # Financial results

            ("results", [
                "financial results",
                "quarterly results",
                "audited results",
                "unaudited results"
            ]),

            # Promoter activity

            ("promoter_purchase", [
                "regulation 29(2)",
                "regulation 7(2)",
                "acquisition of shares",
                "promoter acquired",
                "insider trading regulations",
                "sebi (pit)",
                "pit regulations"
            ]),

            # Meetings

            ("board_meeting", [
                "board meeting"
            ]),

            ("agm", [
                "annual general meeting",
                "agm"
            ]),

            ("egm", [
                "extraordinary general meeting",
                "egm"
            ]),

            ("investor_meeting", [
                "analyst meet",
                "investor meet",
                "investor meeting",
                "analyst / investor meet",
                "investor presentation"
            ]),

            # Reports

            ("annual_report", [
                "annual report"
            ]),

            ("postal_ballot", [
                "postal ballot",
                "scrutinizer report"
            ]),

            ("credit_rating", [
                "credit rating",
                "rating upgrade",
                "rating downgrade"
            ]),

            ("press_release", [
                "press release",
                "media release"
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