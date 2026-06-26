import os
from pathlib import Path

from flask import Flask, render_template

from dashboard.data_service import DashboardDataService
from repository.stock_repository import StockRepository

app = Flask(__name__)

ROOT_DIR = Path(__file__).resolve().parent.parent

dashboard = DashboardDataService()


@app.route("/")
def home():

    summary = dashboard.get_summary()

    return render_template(
        "home.html",
        summary=summary
    )


@app.route("/recent")
def recent():

    rows = dashboard.get_recent_announcements()

    return render_template(
        "recent.html",
        rows=rows
    )


@app.route("/strong_buy")
def strong_buy():

    rows = dashboard.get_strong_buy()

    return render_template(
        "strong_buy.html",
        rows=rows
    )


@app.route("/action_center")
def action_center():

    rows = dashboard.get_action_center()

    cards = []

    for row in rows:

        company_name = row[1]

        stock = StockRepository.get_stock(
            company_name=company_name
        )

        symbol = ""
        tradingview = ""
        screener = ""

        if stock:

            symbol = stock.get("symbol", "")

            tradingview = StockRepository.get_tradingview_url(
                company_name
            )

            screener = StockRepository.get_screener_url(
                company_name
            )

        cards.append(

            {

                "time": row[0],

                "company": company_name,

                "scrip": row[2],

                "headline": row[3],

                "event": row[4],

                "impact": row[5],

                "alpha": row[6],

                "signal": row[7],

                "pdf": row[8],

                "symbol": symbol,

                "sector": "",

                "industry": "",

                "market_cap": "",

                "tradingview": tradingview,

                "screener": screener

            }

        )

    return render_template(

        "action_center.html",

        cards=cards

    )
@app.route("/open_pdf/<path:filename>")
def open_pdf(filename):

    file_path = ROOT_DIR / filename

    if file_path.exists():

        os.startfile(file_path)

        return """
        <html>
        <body>
            <h3>PDF opened successfully.</h3>

            <script>
                window.close();
            </script>

        </body>
        </html>
        """

    return f"""
    <html>
    <body>

        <h3>PDF not found</h3>

        <p>{file_path}</p>

    </body>
    </html>
    """


if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )