from analysis.statistics_engine import StatisticsEngine

engine = StatisticsEngine()

print()

print("Total announcements:")
print(engine.get_total_announcements())

print()

print("Event counts:")
print(engine.get_event_counts())

print()

print("Average alpha:")
print(engine.get_average_alpha_score())

print()

print("Alpha signals:")
print(engine.get_alpha_signal_counts())