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

from analysis.adaptive_scoring_engine import (
    AdaptiveScoringEngine
)

engine = (
    AdaptiveScoringEngine()
)

print(

    engine.get_adjustment(

        "acquisition"

    )

)