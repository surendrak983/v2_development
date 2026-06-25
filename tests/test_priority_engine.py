from analysis.priority_engine import PriorityEngine

engine = PriorityEngine()

events = [
    "order_win",
    "promoter_purchase",
    "fund_raise",
    "dividend",
    "board_meeting",
    "unknown_event"
]

print()

print("EVENT                PRIORITY")
print("-----------------------------")

for event in events:

    priority = engine.get_priority(event)

    print(f"{event:20}{priority}")