import streamlit as st
import pandas as pd

from dashboard.data_service import DashboardDataService


st.title(
    "🔥 Strong Buy Screener"
)

service = DashboardDataService()

rows = service.get_strong_buy()

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

            "Signal"

        ]

    )

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )

else:

    st.info(
        "No Strong Buy signals found."
    )