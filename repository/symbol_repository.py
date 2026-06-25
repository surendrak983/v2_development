class SymbolRepository:

    SYMBOL_MAP = {

        "524804": "AUROPHARMA",

        "500325": "RELIANCE",

        "500209": "INFY",

        "532540": "TCS",

        "500180": "HDFCBANK",

        "500112": "SBIN"

    }

    @classmethod
    def get_symbol(
        cls,
        scrip_code,
        company_name=None
    ):

        scrip_code = str(
            scrip_code
        )

        # First check manual mapping

        symbol = cls.SYMBOL_MAP.get(
            scrip_code
        )

        if symbol:

            return symbol

        # Fallback from company name

        if company_name:

            symbol = (
                company_name
                .replace("Ltd", "")
                .replace("Limited", "")
                .replace("&", "")
                .replace(".", "")
                .replace("-", "")
                .replace(" ", "")
                .upper()
            )

            return symbol

        return None