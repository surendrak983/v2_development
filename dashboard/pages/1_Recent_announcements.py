import os

import pandas as pd
import streamlit as st

from dashboard.data_service import DashboardDataService
from repository.symbol_repository import SymbolRepository


st.title(
    "🎯 Action Center"
)

st.caption(
    "Latest STRONG_BUY opportunities"
)

service = DashboardDataService()

rows = service.get_action_center()

if rows:

    df = pd.DataFrame(

        rows,

        columns=[

            "Time",

            "Company",

            "Scrip",

            "Headline",

            "Event",

            "Impact",

            "Alpha",

            "Signal",

            "PDF"

        ]

    )

    # ----------------------
    # Search
    # ----------------------

    search_text = st.text_input(
        "🔍 Search Company"
    )

    if search_text:

        df = df[
            df["Company"].str.contains(
                search_text,
                case=False,
                na=False
            )
        ]

    # ----------------------
    # Sort
    # ----------------------

    sort_by = st.selectbox(

        "Sort By",

        [

            "Alpha",

            "Time",

            "Company"

        ]

    )

    ascending = False

    if sort_by == "Company":

        ascending = True

    df = df.sort_values(

        by=sort_by,

        ascending=ascending

    )

    # ----------------------
    # Cards
    # ----------------------

    for index, row in df.iterrows():

        st.subheader(
            row["Company"]
        )

        col1, col2 = st.columns(
            2
        )

        with col1:

            st.write(
                "📌 Scrip :",
                row["Scrip"]
            )

            st.write(
                "📌 Event :",
                row["Event"]
            )

            st.write(
                "📌 Alpha :",
                row["Alpha"]
            )

            st.write(
                "📌 Signal :",
                row["Signal"]
            )

        with col2:

            st.write(
                "🕒 Time :",
                row["Time"]
            )

            st.write(
                "⚡ Impact :",
                row["Impact"]
            )

        st.write(
            "📰 Headline"
        )

        st.info(
            row["Headline"]
        )

        symbol = SymbolRepository.get_symbol(
            row["Scrip"]
        )

        c1, c2, c3, c4 = st.columns(
            4
        )

        # ----------------------
        # TradingView
        # ----------------------

        with c1:

            if symbol:

                tv_url = (

                    f"https://in.tradingview.com/chart/?symbol=NSE:{symbol}"

                )

                st.link_button(

                    "📈 TradingView",

                    tv_url

                )

        # ----------------------
        # PDF
        # ----------------------

        with c2:

            if row["PDF"]:

                if st.button(

                    "📄 Open PDF",

                    key=f"pdf_{index}"

                ):

                    pdf_path = os.path.abspath(
                        row["PDF"]
                    )

                    if os.path.exists(
                        pdf_path
                    ):

                        os.startfile(
                            pdf_path
                        )

                    else:

                        st.error(
                            "PDF file not found"
                        )

        # ----------------------
        # Screener
        # ----------------------

        with c3:

            if symbol:

                screener_url = (

                    f"https://www.screener.in/company/{symbol}/"

                )

                st.link_button(

                    "📊 Screener",

                    screener_url

                )

        # ----------------------
        # Moneycontrol
        # ----------------------

        with c4:

            st.link_button(

                "💰 Moneycontrol",

                "https://www.moneycontrol.com/"

            )

        st.divider()

else:

    st.info(

        "No STRONG_BUY opportunities found."

    )