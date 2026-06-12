from pathlib import Path
import sys

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(PROJECT_ROOT)
    )

from services.morning_report_service import (  # noqa: E402
    MorningReportService
)


def _priority_rows(snapshot):

    rows = []

    for item in snapshot["high_priority"]:

        ann = item["announcement"]
        context = item["context"]
        bse_cash = context.get("bse_cash") or {}
        nse_cash = context.get("nse_cash") or {}
        futures = context.get("futures") or {}
        options = context.get("options") or {}
        technical = context.get("technical") or {}
        bias = item["bias"]

        rows.append({
            "Company": ann.get("company_name"),
            "BSE Code": ann.get("scrip_code"),
            "Symbol": context.get("symbol"),
            "Event": ann.get("event_type"),
            "Signal": ann.get("trade_signal"),
            "Impact": ann.get("impact_score"),
            "Ann Time": ann.get("announcement_time"),
            "BSE Date": bse_cash.get("trade_date"),
            "BSE Close": bse_cash.get("close"),
            "1D %": bse_cash.get("return_1d_pct"),
            "Vol x20": bse_cash.get("volume_ratio_20"),
            "NSE Date": nse_cash.get("trade_date"),
            "F&O Date": futures.get("trade_date"),
            "PCR": options.get("put_call_oi_ratio"),
            "Tech Date": technical.get("date"),
            "RSI": technical.get("rsi"),
            "ADX": technical.get("adx"),
            "Bias": bias.get("bias"),
            "Reason": ", ".join(
                bias.get("reasons") or []
            ),
            "Headline": ann.get("headline"),
        })

    return rows


def _latest_rows(snapshot):

    rows = []

    for row in snapshot["latest_announcements"]:

        rows.append({
            "Time": row.get("announcement_time"),
            "Company": row.get("company_name"),
            "BSE Code": row.get("scrip_code"),
            "Event": row.get("event_type"),
            "Signal": row.get("trade_signal"),
            "Impact": row.get("impact_score"),
            "Headline": row.get("headline"),
        })

    return rows


st.set_page_config(
    page_title="8 AM Market Setup",
    layout="wide"
)

st.title("8 AM Market Setup")

with st.sidebar:
    st.header("Controls")
    limit = st.slider(
        "Priority rows",
        min_value=5,
        max_value=100,
        value=25,
        step=5
    )

    refresh = st.button(
        "Refresh"
    )

service = MorningReportService()
snapshot = service.build_snapshot(
    limit=limit
)

generated_at = snapshot["generated_at"]

st.caption(
    f"Generated at {generated_at:%Y-%m-%d %H:%M:%S}"
)

priority_rows = _priority_rows(snapshot)
latest_rows = _latest_rows(snapshot)

strong_count = sum(
    1
    for row in priority_rows
    if row.get("Signal") == "STRONG_BUY"
)

watch_count = sum(
    1
    for row in priority_rows
    if row.get("Signal") in ("BUY_CANDIDATE", "WATCH")
)

staleness_count = sum(
    1
    for row in priority_rows
    if row.get("BSE Date") != row.get("F&O Date")
    or row.get("F&O Date") != row.get("Tech Date")
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Priority Items",
    len(priority_rows)
)

col2.metric(
    "Strong Buy",
    strong_count
)

col3.metric(
    "Buy/Watch",
    watch_count
)

col4.metric(
    "Freshness Warnings",
    staleness_count
)

tabs = st.tabs([
    "Priority",
    "Latest",
    "Event Mix",
    "Saved Report"
])

with tabs[0]:
    st.subheader("Priority BSE Announcements")

    if priority_rows:
        st.dataframe(
            pd.DataFrame(priority_rows),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info(
            "No priority announcements found."
        )

    st.caption(
        "Freshness warnings rise when BSE cash, NSE F&O, or technical JSON dates do not match."
    )

with tabs[1]:
    st.subheader("Latest BSE Announcements")
    st.dataframe(
        pd.DataFrame(latest_rows),
        use_container_width=True,
        hide_index=True
    )

with tabs[2]:
    st.subheader("Event Mix")

    left, right = st.columns(2)

    with left:
        st.write("Recent Event Types")
        st.dataframe(
            pd.DataFrame(
                snapshot["event_counts"].items(),
                columns=["Event", "Count"]
            ),
            hide_index=True,
            use_container_width=True
        )

    with right:
        st.write("All Stored Signal Types")
        st.dataframe(
            pd.DataFrame(
                snapshot["signal_counts"].items(),
                columns=["Signal", "Count"]
            ),
            hide_index=True,
            use_container_width=True
        )

with tabs[3]:
    st.subheader("Generate Markdown Report")

    if st.button(
        "Write report file"
    ):
        path = service.write_markdown_report(
            limit=limit
        )
        st.success(
            f"Report written: {path}"
        )

    markdown = service.render_markdown(
        snapshot
    )

    st.download_button(
        "Download current report",
        markdown,
        file_name=f"market_setup_{generated_at:%Y%m%d_%H%M%S}.md",
        mime="text/markdown"
    )

    st.markdown(markdown)

if refresh:
    st.rerun()
