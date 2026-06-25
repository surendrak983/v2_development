
import streamlit as st

from services.service_manager import ServiceManager


st.title(
    "⚙️ Control Center"
)

manager = ServiceManager()

manager.initialize_service(
    "monitor",
    interval=60
)

manager.initialize_service(
    "analysis",
    interval=60
)

manager.initialize_service(
    "statistics",
    interval=600
)

# =====================================================
# MONITOR
# =====================================================

st.subheader(
    "Announcement Monitor"
)

info = manager.get_info(
    "monitor"
)

st.write(
    "Status:",
    "🟢 Running" if info["running"] else "🔴 Stopped"
)

st.write(
    "Interval:",
    info["interval"],
    "sec"
)

st.write(
    "Last Run:",
    info["last_run"]
)

st.write(
    "Records Processed:",
    info["records_processed"]
)

st.write(
    "Errors:",
    info["error_count"]
)

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "Start Monitor"
    ):

        manager.start_service(
            "monitor"
        )

        st.rerun()

with col2:

    if st.button(
        "Stop Monitor"
    ):

        manager.stop_service(
            "monitor"
        )

        st.rerun()

with col3:

    if st.button(
        "Run Monitor Now"
    ):

        manager.run_now(
            "monitor"
        )

        st.rerun()

st.divider()

# =====================================================
# ANALYSIS
# =====================================================

st.subheader(
    "Analysis Engine"
)

info = manager.get_info(
    "analysis"
)

st.write(
    "Status:",
    "🟢 Running" if info["running"] else "🔴 Stopped"
)

st.write(
    "Interval:",
    info["interval"],
    "sec"
)

st.write(
    "Last Run:",
    info["last_run"]
)

st.write(
    "Records Processed:",
    info["records_processed"]
)

st.write(
    "Errors:",
    info["error_count"]
)

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "Start Analysis"
    ):

        manager.start_service(
            "analysis"
        )

        st.rerun()

with col2:

    if st.button(
        "Stop Analysis"
    ):

        manager.stop_service(
            "analysis"
        )

        st.rerun()

with col3:

    if st.button(
        "Run Analysis Now"
    ):

        manager.run_now(
            "analysis"
        )

        st.rerun()

st.divider()

# =====================================================
# STATISTICS
# =====================================================

st.subheader(
    "Statistics Engine"
)

info = manager.get_info(
    "statistics"
)

st.write(
    "Status:",
    "🟢 Running" if info["running"] else "🔴 Stopped"
)

st.write(
    "Interval:",
    info["interval"],
    "sec"
)

st.write(
    "Last Run:",
    info["last_run"]
)

st.write(
    "Records Processed:",
    info["records_processed"]
)

st.write(
    "Errors:",
    info["error_count"]
)

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "Start Statistics"
    ):

        manager.start_service(
            "statistics"
        )

        st.rerun()

with col2:

    if st.button(
        "Stop Statistics"
    ):

        manager.stop_service(
            "statistics"
        )

        st.rerun()

with col3:

    if st.button(
        "Run Statistics Now"
    ):

        manager.run_now(
            "statistics"
        )

        st.rerun()

