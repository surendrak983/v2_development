from analysis.impact_engine import (
    ImpactEngine
)

engine = ImpactEngine()

tests = [

    {
        "event_type": "acquisition",
        "stake_percent": 60
    },

    {
        "event_type": "dividend",
        "dividend": 12
    },

    {
        "event_type": "unknown"
    },

    {
        "event_type": "board_meeting"
    }

]

for x in tests:

    result = engine.score(
        x
    )

    print(
        x["event_type"],
        result
    )