from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class BhavcopyDownloader:

    @staticmethod
    def build_url(trade_date):

        ymd = trade_date.strftime("%Y%m%d")

        return (
            "https://www.bseindia.com/download/BhavCopy/Equity/"
            f"BhavCopy_BSE_CM_0_0_0_{ymd}_F_0000.CSV"
        )

    def download_csv(self, trade_date):

        url = self.build_url(trade_date)

        print(f"Downloading {trade_date:%d-%m-%Y}")

        request = Request(
            url,
            headers={
                "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Accept":
                    "text/csv,*/*"
            }
        )

        try:

            with urlopen(request, timeout=60) as response:

                content_type = response.headers.get(
                    "Content-Type",
                    ""
                )

                raw = response.read()

        except HTTPError as exc:

            print(f"HTTP error {exc.code}")
            return None

        except URLError as exc:

            print(f"Download failed: {exc.reason}")
            return None

        except TimeoutError:

            print("Download timeout")
            return None

        text = raw.decode(
            "utf-8-sig",
            errors="replace"
        )

        if (
            "text/html" in content_type.lower()
            or
            text.lstrip().lower().startswith("<!doctype")
        ):
            return None

        return text