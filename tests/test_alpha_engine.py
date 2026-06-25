from analysis.alpha_engine import (
    AlphaEngine
)


engine = AlphaEngine()

tests = [

    (
        100,
        95,
        1
    ),

    (
        85,
        90,
        2
    ),

    (
        55,
        70,
        4
    )

]

print()

print(
    f"{'IMPACT':>8}"
    f"{'CONF':>8}"
    f"{'PRIOR':>8}"
    f"{'ALPHA':>8}"
)

print("-" * 32)

for impact_score, confidence, priority in tests:

    alpha_score = engine.calculate(
        impact_score,
        confidence,
        priority
    )

    print(
        f"{impact_score:>8}"
        f"{confidence:>8}"
        f"{priority:>8}"
        f"{alpha_score:>8}"
    )