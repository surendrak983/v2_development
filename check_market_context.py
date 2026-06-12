import argparse
import json

from repository.market_context_repository import (
    MarketContextRepository
)


def main():

    parser = argparse.ArgumentParser(
        description="Inspect market context from BSE cash and NSE F&O projects."
    )

    parser.add_argument(
        "--scrip-code",
        help="BSE scrip code, e.g. 500325"
    )

    parser.add_argument(
        "--symbol",
        help="NSE symbol, e.g. RELIANCE"
    )

    args = parser.parse_args()

    repo = MarketContextRepository()

    context = repo.get_context(
        scrip_code=args.scrip_code,
        symbol=args.symbol
    )

    print(
        json.dumps(
            context,
            indent=2,
            default=str
        )
    )


if __name__ == "__main__":
    main()
