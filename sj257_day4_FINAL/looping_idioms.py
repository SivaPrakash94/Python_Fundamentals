""" Learn the common patterns for looping in Python

Styles
-----------------------
IMPERATIVE PROGRAMMING:   Tells HOW to do something
DECLARATIVE PROGRAMMING:  Describes WHAT is being done
FUNCTIONAL PROGRAMMING:   Nested functions (no for-loops or variables)

"""

from itertools import zip_longest

names = 'raymond rachel matthew'.split()
colors = 'red blue yellow green'.split()
cities = 'austin dallas chicago austin houston austin chicago dallas'.split()

print('Task 1: Show all of the names in a different case')

for i in range(len(names)):
    print(names[i].upper())

for name in names:
    print(name.title())

print('\nTask 2: Show all the colors AND their ordinal position')

for i in range(len(colors)):
    print(i+1, '-->', colors[i])

for i, color in enumerate(colors, start=1):
    print(i, '-->', color)

print('\nTask 3:  Show all of names in reverse order')

for i in range(len(names)-1, -1, -1):
    print(names[i].upper())

for name in reversed(names):
    print(name.title())

print('\nTask 4: Show the names and colors pairwise, ignoring mismatches')

nn = len(names)
nc = len(colors)
n = nn
if nc < n:
    n = nc
for i in range(n):
    print(names[i], '-->', colors[i])

nn = len(names)
nc = len(colors)
n = nn if nn < nc else nc    # ternary operator -- conditional expression
for i in range(n):
    print(names[i], '-->', colors[i])

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i])

for name, color in zip(names, colors):
    print(name, '-->', color)

print('\nTask 5: Show the names and colors pairwise, keeping mismatches')

for name, color in zip_longest(names, colors, fillvalue='unknown'):
    print(name, '-->', color)

print('\nTask 6: Show the colors alphabetically')

for color in sorted(colors):
    print(color)

print('\nTask 7: Show the colors arranged shortest to longest')
print('SELECT color FROM Colors ORDER BY LENGTH(color);')

for color in sorted(colors, key=len):
    print(color)

print('\nTask 8: Show the colors arranged by the third letter')
print('SELECT color FROM Colors ORDER BY SUBSTRING(color, 3, 1);')

for color in sorted(colors, key=lambda w: w[2]):
    print(color)

print('\nTask 9: Show the colors arranged by decreasing length')
print('SELECT color FROM Colors ORDER BY LENGTH(color) DESCENDING;')

for color in sorted(colors, key=len, reverse=True):
    print(color)

print('\nTask 10: Show and number all the cities alphabetically without dups')
print('SELECT AUTONUM(), "-->", DISTINCT city FROM Cities ORDER BY city;')

for i, city in enumerate(sorted(set(cities)), start=1):
    print(i, '-->', city)

