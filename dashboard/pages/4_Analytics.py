
import streamlit as st
import pandas as pd
import plotly.express as px

from dashboard.data_service import DashboardDataService


st.title(
    "📈 Analytics"
)

service = DashboardDataService()

st.subheader(
    "Average Alpha By Event"
)

rows = service.get_average_alpha_by_event()

if rows:

    df = pd.DataFrame(
        rows,
        columns=[
            "Event",
            "Average Alpha"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    fig = px.bar(
        df,
        x="Event",
        y="Average Alpha",
        title="Average Alpha Score by Event"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info(
        "No analytics available."
    )

