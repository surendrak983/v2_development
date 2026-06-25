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

from analysis.entity_extractor import (
    EntityExtractor
)

extractor = EntityExtractor()

text = """
Company acquired 74% stake in XYZ Ltd and declared
interim dividend of Rs. 12 per share.
"""

result = extractor.extract(
    text
)

print(result)