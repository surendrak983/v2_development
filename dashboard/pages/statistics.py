
import streamlit as st
import pandas as pd

from dashboard.data_service import DashboardDataService

st.title(
    "📰 Recent Announcements"
)

service = DashboardDataService()

rows = service.get_recent_announcements()

if rows:

    df = pd.DataFrame(
        rows,
        columns=[
            "Time",
            "Event",
            "Impact",
            "Alpha",
            "Signal"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.info(
        "No records available."
    )

