import re
from pprint import pp
from statistics import mean, median, stdev

with open('data/team_history.txt') as f:
    hist = f.read()
    #print(hist)
    #pp(history)

re.findall(r'\d+/\d+/\d+', hist)
scores = list(map(int, re.findall(r'(\d+) (?:point|goal)s?',hist)))
dates = re.findall(r'\d{1,2}/\d{1,2}/\d{4}', hist)
record = re.findall(r'won|lost', hist)

#print(f'In 2013, we played {len(dates)} games from {dates[0]} to {dates[-1]}')


with open('data/parse_demo1.txt') as f1:
    extract = f1.read()

print(extract)
