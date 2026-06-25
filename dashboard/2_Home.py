
import streamlit as st

from dashboard.data_service import DashboardDataService

st.title("🏠 Home")

service = DashboardDataService()

summary = service.get_summary()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Announcements",
        summary["total_announcements"]
    )

with col2:
    st.metric(
        "Average Alpha",
        summary["average_alpha"]
    )

with col3:
    st.metric(
        "STRONG_BUY",
        summary["strong_buy_count"]
    )

with col4:
    st.metric(
        "BUY",
        summary["buy_count"]
    )

