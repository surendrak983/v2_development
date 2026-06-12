import argparse

from services.morning_report_service import (
    MorningReportService
)


def main():

    parser = argparse.ArgumentParser(
        description="Generate the 8 AM market setup report."
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        help="Number of priority announcements to include."
    )

    args = parser.parse_args()

    service = MorningReportService()

    report_path = service.write_markdown_report(
        limit=args.limit
    )

    print(
        f"Report written: {report_path}"
    )


if __name__ == "__main__":
    main()
