import yfinance as yf


class MarketDataService:

    @staticmethod
    def get_snapshot(symbol):

        try:

            ticker = yf.Ticker(
                symbol + ".NS"
            )

            info = ticker.info

            return {

                "cmp": info.get(
                    "currentPrice"
                ),

                "change_percent": info.get(
                    "regularMarketChangePercent"
                ),

                "volume": info.get(
                    "volume"
                ),

                "sector": info.get(
                    "sector"
                ),

                "market_cap": info.get(
                    "marketCap"
                )

            }

        except Exception:

            return None