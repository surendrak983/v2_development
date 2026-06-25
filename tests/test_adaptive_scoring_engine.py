from analysis.adaptive_scoring_engine import (
    AdaptiveScoringEngine
)


engine = AdaptiveScoringEngine()

events = [
    "acquisition",
    "investor_meeting",
    "dividend",
    "unknown",
    "board_meeting"
]

print()

print(
    f"{'EVENT TYPE':20}"
    f"{'ADJUSTMENT':>12}"
)

print("-" * 32)

for event in events:

    adjustment = engine.get_adjustment(
        event
    )

    print(
        f"{event:20}"
        f"{adjustment:>12}"
    )