from datetime import datetime


class BSEClient:

    def get_announcements(self):

        return [
            {
                "exchange_id": "BSE_TEST_001",
                "scrip_code": "500325",
                "company_name": "Reliance Industries",
                "headline": "Board Meeting to Consider Fund Raising",
                "announcement_time": datetime.now().isoformat()
            }
        ]