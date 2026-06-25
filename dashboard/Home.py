
import streamlit as st

from dashboard.data_service import DashboardDataService


st.set_page_config(
    page_title="BSE V2 Market Intelligence Dashboard",
    layout="wide"
)

st.title(
    "📈 BSE V2 Market Intelligence Dashboard"
)

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

st.divider()

st.subheader(
    "Welcome to BSE V2 Market Intelligence Platform"
)

st.markdown(
"""
Use the sidebar to navigate:

- 📰 Recent Announcements
- 🔥 Strong Buy Screener
- 📊 Charts
- 📈 Analytics
"""
)

