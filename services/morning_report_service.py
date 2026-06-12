from collections import Counter
from datetime import datetime

from core.config import REPORT_DIR
from repository.market_context_repository import (
    MarketContextRepository
)
from repository.morning_report_repository import (
    MorningReportRepository
)


def _fmt(value):

    if value is None:
        return "N/A"

    if isinstance(value, float):
        return f"{value:.2f}"

    return str(value)


def _freshness_label(date_value):

    if not date_value:
        return "N/A"

    return str(date_value)


def _bias_from_context(context):

    technical = context.get("technical") or {}
    bse_cash = context.get("bse_cash") or {}
    options = context.get("options") or {}

    score = 0
    reasons = []

    return_1d = bse_cash.get("return_1d_pct")
    volume_ratio = bse_cash.get("volume_ratio_20")
    rsi = technical.get("rsi")
    supertrend_dir = technical.get("supertrend_dir")
    pcr = options.get("put_call_oi_ratio")

    if return_1d is not None:
        if return_1d > 1:
            score += 1
            reasons.append("positive close")
        elif return_1d < -1:
            score -= 1
            reasons.append("weak close")

    if volume_ratio is not None and volume_ratio >= 1.5:
        reasons.append(f"volume {volume_ratio}x 20-day average")

    if rsi is not None:
        if rsi >= 60:
            score += 1
            reasons.append("RSI strong")
        elif rsi <= 35:
            score -= 1
            reasons.append("RSI weak/oversold")

    if supertrend_dir == 1:
        score += 1
        reasons.append("supertrend positive")
    elif supertrend_dir == -1:
        score -= 1
        reasons.append("supertrend negative")

    if pcr is not None:
        if pcr >= 1.2:
            score += 1
            reasons.append("supportive put-call OI")
        elif pcr <= 0.7:
            score -= 1
            reasons.append("call-heavy option OI")

    if score >= 2:
        bias = "Bullish"
    elif score <= -2:
        bias = "Bearish"
    else:
        bias = "Neutral"

    return {
        "bias": bias,
        "score": score,
        "reasons": reasons[:4],
    }


class MorningReportService:

    def __init__(self):

        self.report_repo = MorningReportRepository()
        self.context_repo = MarketContextRepository()

    def build_snapshot(
        self,
        limit=25
    ):

        high_priority = (
            self.report_repo
            .get_high_priority_announcements(
                limit=limit
            )
        )

        latest = (
            self.report_repo
            .get_latest_announcements(
                limit=limit
            )
        )

        enriched = []

        for row in high_priority:

            context = self.context_repo.get_context(
                scrip_code=row.get("scrip_code")
            )

            enriched.append({
                "announcement": row,
                "context": context,
                "bias": _bias_from_context(context),
            })

        event_counts = Counter(
            row.get("event_type") or "unknown"
            for row in latest
        )

        signal_counts = self.report_repo.get_signal_counts()

        return {
            "generated_at": datetime.now(),
            "latest_announcements": latest,
            "high_priority": enriched,
            "event_counts": dict(event_counts),
            "signal_counts": signal_counts,
        }

    def render_markdown(
        self,
        snapshot
    ):

        generated_at = snapshot["generated_at"]

        lines = [
            "# 8 AM Market Setup",
            "",
            f"Generated: {generated_at:%Y-%m-%d %H:%M:%S}",
            "",
            "## Priority BSE Announcements",
            "",
        ]

        if not snapshot["high_priority"]:
            lines.append("No priority announcements found.")
        else:
            lines.extend([
                "| Company | Event | Signal | BSE Date | BSE Close | 1D % | Vol x | NSE F&O Date | Technical Date | Bias |",
                "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
            ])

            for item in snapshot["high_priority"]:

                ann = item["announcement"]
                context = item["context"]
                bse_cash = context.get("bse_cash") or {}
                futures = context.get("futures") or {}
                technical = context.get("technical") or {}
                bias = item["bias"]

                lines.append(
                    "| "
                    + " | ".join([
                        ann.get("company_name") or "N/A",
                        ann.get("event_type") or "unknown",
                        ann.get("trade_signal") or "N/A",
                        _freshness_label(bse_cash.get("trade_date")),
                        _fmt(bse_cash.get("close")),
                        _fmt(bse_cash.get("return_1d_pct")),
                        _fmt(bse_cash.get("volume_ratio_20")),
                        _freshness_label(futures.get("trade_date")),
                        _freshness_label(technical.get("date")),
                        bias["bias"],
                    ])
                    + " |"
                )

        lines.extend([
            "",
            "## Bias Notes",
            "",
        ])

        for item in snapshot["high_priority"]:

            ann = item["announcement"]
            bias = item["bias"]
            reasons = ", ".join(bias["reasons"]) or "no strong context signal"

            lines.append(
                f"- {ann.get('company_name')}: {bias['bias']} "
                f"({reasons})"
            )

        lines.extend([
            "",
            "## Latest Announcements",
            "",
            "| Time | Company | Headline | Event | Signal |",
            "|---|---|---|---|---|",
        ])

        for row in snapshot["latest_announcements"][:20]:
            headline = (
                row.get("headline") or ""
            ).replace("|", "/")

            lines.append(
                "| "
                + " | ".join([
                    _fmt(row.get("announcement_time")),
                    row.get("company_name") or "N/A",
                    headline[:160],
                    row.get("event_type") or "unknown",
                    row.get("trade_signal") or "N/A",
                ])
                + " |"
            )

        lines.extend([
            "",
            "## Event Mix",
            "",
        ])

        for event_type, count in snapshot["event_counts"].items():
            lines.append(f"- {event_type}: {count}")

        lines.extend([
            "",
            "## Signal Mix",
            "",
        ])

        for signal, count in snapshot["signal_counts"].items():
            lines.append(f"- {signal}: {count}")

        lines.extend([
            "",
            "## Operating Notes",
            "",
            "- Refresh BSE cash EOD after your 9 PM BSE job.",
            "- Refresh NSE cash/futures/options and technical JSON before relying on F&O/technical context.",
            "- Treat stale source dates as a warning, not as a trading signal.",
        ])

        return "\n".join(lines) + "\n"

    def write_markdown_report(
        self,
        limit=25
    ):

        snapshot = self.build_snapshot(
            limit=limit
        )

        markdown = self.render_markdown(
            snapshot
        )

        report_path = (
            REPORT_DIR
            / f"market_setup_{snapshot['generated_at']:%Y%m%d_%H%M%S}.md"
        )

        report_path.write_text(
            markdown,
            encoding="utf-8"
        )

        return report_path
