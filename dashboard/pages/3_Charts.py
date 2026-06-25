
import streamlit as st
import pandas as pd
import plotly.express as px

from dashboard.data_service import DashboardDataService


st.title(
    "📊 Charts"
)

service = DashboardDataService()


# Event Frequency

st.subheader(
    "Event Frequency"
)

event_rows = service.get_event_counts()

if event_rows:

    df_event = pd.DataFrame(
        event_rows,
        columns=[
            "Event",
            "Count"
        ]
    )

    fig = px.bar(
        df_event,
        x="Event",
        y="Count",
        title="Event Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# Alpha Signal Distribution

st.subheader(
    "Alpha Signal Distribution"
)

alpha_rows = service.get_alpha_signal_counts()

if alpha_rows:

    df_alpha = pd.DataFrame(
        alpha_rows,
        columns=[
            "Signal",
            "Count"
        ]
    )

    fig = px.pie(
        df_alpha,
        names="Signal",
        values="Count"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

