import os
from pathlib import Path

from flask import Flask, render_template

from dashboard.data_service import DashboardDataService
from repository.symbol_repository import SymbolRepository
from repository.company_repository import CompanyRepository

app = Flask(__name__)

ROOT_DIR = Path(__file__).resolve().parent.parent


@app.route("/")
def home():

    summary = DashboardDataService().get_summary()

    return render_template(
        "home.html",
        summary=summary
    )


@app.route("/recent")
def recent():

    rows = DashboardDataService().get_recent_announcements()

    return render_template(
        "recent.html",
        rows=rows
    )


@app.route("/strong_buy")
def strong_buy():

    rows = DashboardDataService().get_strong_buy()

    return render_template(
        "strong_buy.html",
        rows=rows
    )


@app.route("/action_center")
def action_center():

    rows = DashboardDataService().get_action_center()

    cards = []

    for row in rows:

        scrip = str(row[2])

        symbol = SymbolRepository.get_symbol(
            scrip
        )

        info = CompanyRepository.get_company_info(
            scrip
        )

        cards.append(

            {

                "time": row[0],

                "company": row[1],

                "scrip": scrip,

                "headline": row[3],

                "event": row[4],

                "impact": row[5],

                "alpha": row[6],

                "signal": row[7],

                "pdf": row[8],

                "symbol": symbol,

                "sector": info["sector"],

                "industry": info["industry"],

                "market_cap": info["market_cap"]

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

        <h2>

        PDF opened successfully.

        </h2>

        <script>

        window.close();

        </script>

        """

    return f"""

    <h2>

    PDF not found

    </h2>

    <p>

    {file_path}

    </p>

    """


if __name__ == "__main__":

    app.run(
        debug=True
    )