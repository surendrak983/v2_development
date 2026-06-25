import re


class EntityExtractor:

    def extract(
        self,
        text
    ):

        if not text:

            return {}

        entities = {}

        text = text.lower()

        # ----------------------------
        # Order value
        # ----------------------------

        patterns = [

            r'rs\.?\s*([\d,\.]+)\s*crore',
            r'₹\s*([\d,\.]+)\s*crore'

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text
            )

            if match:

                try:

                    entities[
                        "amount_crore"
                    ] = float(
                        match.group(1)
                        .replace(
                            ",",
                            ""
                        )
                    )

                    break

                except:

                    pass

        # ----------------------------
        # Stake %
        # ----------------------------

        match = re.search(

            r'([\d\.]+)\s*%',

            text
        )

        if match:

            try:

                entities[
                    "stake_percent"
                ] = float(
                    match.group(1)
                )

            except:

                pass

        # ----------------------------
        # Dividend
        # ----------------------------

        match = re.search(

            r'dividend.*?rs\.?\s*([\d\.]+)',

            text
        )

        if match:

            try:

                entities[
                    "dividend"
                ] = float(
                    match.group(1)
                )

            except:

                pass

        # ----------------------------
        # Rating
        # ----------------------------

        rating_match = re.search(

            r'\b(aaa|aa\+|aa|a\+|a)\b',

            text
        )

        if rating_match:

            entities[
                "rating"
            ] = rating_match.group(
                1
            ).upper()

        return entities