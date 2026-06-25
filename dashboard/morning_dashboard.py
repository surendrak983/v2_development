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


def _source_count_label(section):

    count = len(section["sources"])

    return f"{count} source" if count == 1 else f"{count} sources"


def _source_badge(source_type):

    class_name = f"source-badge badge-{source_type.lower()}"

    return f'<span class="{class_name}">{source_type}</span>'


def _source_section_html(section):

    rows = []

    for name, description, source_type in section["sources"]:
        rows.append(
            "<div class='source-row'>"
            f"<div class='source-name'>{name}</div>"
            f"<div class='source-desc'>{description}</div>"
            f"<div class='source-type'>{_source_badge(source_type)}</div>"
            "</div>"
        )

    rows_html = "".join(rows)

    return (
        "<section class='source-section'>"
        "<div class='source-section-head'>"
        "<div class='source-title-wrap'>"
        f"<span class='source-dot' style='background:{section['color']}'></span>"
        f"<h3>{section['title']}</h3>"
        "</div>"
        f"<div class='source-count'>{_source_count_label(section)} <span>▼</span></div>"
        "</div>"
        f"{rows_html}"
        "</section>"
    )


def _render_source_map():

    st.markdown("""
    <style>
        .source-legend {
            display: flex;
            gap: .75rem;
            flex-wrap: wrap;
            margin: .35rem 0 1.25rem;
            align-items: center;
        }
        .legend-item {
            display: inline-flex;
            align-items: center;
            gap: .35rem;
            font-size: .82rem;
            color: #222;
        }
        .source-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 4.3rem;
            padding: .12rem .45rem;
            border-radius: 999px;
            font-size: .72rem;
            font-weight: 700;
            line-height: 1.25;
            white-space: nowrap;
        }
        .badge-primary {
            background: #eaf5d8;
            color: #4d8f1f;
        }
        .badge-secondary {
            background: #faecd5;
            color: #b16d11;
        }
        .badge-signal {
            background: #ece9ff;
            color: #4d46c0;
        }
        .source-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 1.8rem 2.4rem;
            margin-top: .5rem;
        }
        .source-section {
            min-width: 0;
        }
        .source-section-head {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: .85rem;
        }
        .source-title-wrap {
            display: flex;
            align-items: center;
            gap: .55rem;
            min-width: 0;
        }
        .source-dot {
            width: .58rem;
            height: .58rem;
            border-radius: 999px;
            flex: 0 0 auto;
        }
        .source-section h3 {
            margin: 0;
            font-size: 1rem;
            font-weight: 650;
            line-height: 1.2;
            color: #111;
        }
        .source-count {
            display: inline-flex;
            align-items: center;
            gap: .45rem;
            color: #111;
            font-size: .78rem;
            white-space: nowrap;
        }
        .source-count span {
            color: #005aa8;
            font-size: .66rem;
        }
        .source-row {
            display: grid;
            grid-template-columns: minmax(7rem, .8fr) minmax(13rem, 2.25fr) 5.2rem;
            gap: .8rem;
            align-items: center;
            padding: .2rem 0;
            border-bottom: 1px solid rgba(0, 0, 0, .035);
        }
        .source-name {
            font-size: .86rem;
            font-weight: 600;
            color: #111;
            line-height: 1.25;
        }
        .source-desc {
            font-size: .82rem;
            color: #111;
            line-height: 1.3;
        }
        .source-type {
            display: flex;
            justify-content: flex-end;
        }
        @media (max-width: 980px) {
            .source-grid {
                grid-template-columns: 1fr;
            }
            .source-row {
                grid-template-columns: minmax(6.5rem, .85fr) minmax(11rem, 2fr) 5.2rem;
            }
        }
        @media (max-width: 640px) {
            .source-row {
                grid-template-columns: 1fr;
                gap: .15rem;
                padding: .55rem 0;
            }
            .source-type {
                justify-content: flex-start;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    filter_options = [
        "All sources",
        "Regulatory",
        "Market data",
        "Research",
        "Media",
        "Alternative",
        "Insider signals",
    ]

    selected_filter = st.radio(
        "Source category",
        filter_options,
        horizontal=True,
        label_visibility="collapsed"
    )

    legend = "".join(
        "<span class='legend-item'>"
        f"{_source_badge(label)}"
        f"<span>{description}</span>"
        "</span>"
        for label, description in SOURCE_TYPE_LABELS.items()
    )

    st.markdown(
        f"<div class='source-legend'>{legend}</div>",
        unsafe_allow_html=True
    )

    sections = [
        section
        for section in SOURCE_CATALOG
        if selected_filter == "All sources"
        or section["filter"] == selected_filter
    ]

    sections_html = "".join(
        _source_section_html(section)
        for section in sections
    )

    st.markdown(
        f"<div class='source-grid'>{sections_html}</div>",
        unsafe_allow_html=True
    )


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
    "Source Map",
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
    st.subheader("Market Intelligence Source Map")
    _render_source_map()

with tabs[4]:
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
