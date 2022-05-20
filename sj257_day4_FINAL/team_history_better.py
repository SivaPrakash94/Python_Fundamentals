from statistics import mean, median, stdev
from pprint import pprint
import json

with open('data/team_history.json') as f:
    hist = json.load(f)

dates = [game['date'] for game in hist]
record = [game['result'] for game in hist]
scores = [game['score'] for game in hist]

print(f'In 2013, we played {len(dates)} games from {dates[0]} to {dates[-1]}.')
print(f'We scored {sum(scores)} goals in total for an average of {mean(scores)} per game.')
print(f'In at least half of the game we scored at least {median(scores)} times.')
print(f'Our lowest was {min(scores)} and our best was {max(scores)}.')
print(f'Our overall record was {record.count("won")}-{record.count("lost")}.')
print(f'We {record[0]} our first game and {record[-1]} our last game.')
