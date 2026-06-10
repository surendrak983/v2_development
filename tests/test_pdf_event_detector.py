import sys
from pathlib import Path

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)

from analysis.pdf_event_detector import (
    PDFEventDetector
)

detector = (
    PDFEventDetector()
)

samples = [

    """
    Investor Presentation for Analyst /
    Institutional Investor Meeting
    """,

    """
    Company has acquired 74%
    stake in XYZ Limited
    """,

    """
    Company received order worth
    Rs 500 crore from Ministry of Defence
    """,

    """
    Rights Issue Committee Meeting
    """,

    """
    CARE Ratings has reaffirmed
    credit rating of the company
    """
]

for text in samples:

    print()
    print("=" * 60)

    result = detector.detect(
        text
    )

    print(text.strip())

    print(result)