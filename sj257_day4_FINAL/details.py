'''\
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.
'''

# Introspection involves looking at variables
# that describe an object.

print('Name of the module', __name__)
print('Filename:', __file__)
print('Docstring:')
print(__doc__)
print()

if __name__ == '__main__':
    print('I have the default name, so I was NOT imported.\n')
else:
    print('My name changed, so I WAS imported')

#############################################################
## Dict literals are made with curly braces and colons.
## Dicts associate keys with values.
## Keys must be unique (remember the rule of namespaces).
## Values may be duplicated.
## In modern dicts, the insertion order is remembered.
## They are unbelievably fast and scaleable.

kind = {
    'cisco': 'networking',
    'crisco': 'shortening',
    'costco': 'retail',
    'sysco': 'food service',
    'san franscisco': 'municipality',
}

print(type(kind))
print(len(kind))                   # size
print('costco' in kind)            # membership testing
print(kind['cisco'])               # lookup a key to find a value

print(kind.keys())                 # left column before the colon
print(kind.values())               # right column after the colon
print(kind.items())                # key/value pairs

# EAFP: Easier to ask forgiveness than permission
try:
    print(kind['target'])          # Atomic transaction
except KeyError:
    print('target is in an unknown business')

# LBYL:  Look before you leap
if 'target' in kind:
    print(kind['target'])
else:
    print('target is in an unknown business')

# Unconditional looks can't fail because they have default values
print('target is in the', kind.get('target', 'unknown'), 'business')

import os

# Incorrect example that risks a "race condition"
if os.path.exists('tmp.txt'):
    os.remove('tmp.txt')

# Correct example using EAFP
try:
    os.remove('tmp.txt')
except FileNotFoundError:
    pass

# We can also call the dict() constructor with keyword arguments
# This only works for string keys that are valid identifiers
k2 = dict(cisco='networking', sysco='food service',
          san_franscisco='municipality')
print(k2)

#############################################################
## Functions are the key to reusable code
## Functions are the key to managing complexity
## Functions organize our thoughts.
## Functions rock!

import math
import random
import collections
import operator

print(ord('A'))        # builtin functions don't have to be imported
print(chr(65))
print(hex(100))

print(math.cos(3.0))
print(math.log(3.5))
print(math.comb(25, 10))
print(math.perm(25, 10))
print(random.randrange(10_000, 20_000))
print(random.randrange(10_000, 20_000))
print(collections.Counter('simsalbim').most_common(3))
print(operator.add(30, 40))

def cube(x):
    'Return a value times itself thrice.'
    return x * x * x

print(cube(12))
print([cube(0), cube(1), cube(2), cube(3), cube(4),
       cube(5), cube(6), cube(7), cube(8), cube(9),
       cube(10), cube(11), cube(12), cube(13), cube(14)])

# List comprehension:
#  [ <expr> for <var> in <iterable> if <cond> ]
print([cube(n) for n in range(15)])

# map(<func>, <iterable>) -> <iterator>
# list(<iterator>) -> <list>
print(list(map(cube, range(15))))
print(list(map(hex, map(ord, 'Red bull has wiiings'))))

def introspect(func):
    'Look inside a function to find the name, module, and doc'
    print('Name:', func.__name__)
    print('Module:', func.__module__)
    print('Docstring:', func.__doc__)
    print()

introspect(cube)
introspect(introspect)
introspect(ord)
introspect(math.comb)

# The word "def" plain English.
# The word "lambda" is Greek for "make function".
print(list(map(lambda x: 5*x**3 - 15*x**2 - 32*x + 4, range(10))))

#############################################################
# Set literals are made with curly braces but not colons.
# Set elements are unordered and eliminate duplicates.
# They are you number one tool for data analysis
# Three main use cases:
# 1) Deduping
# 2) Fast membership testing
# 3) Set-to-set operations
# Many complex analysis problems can be expressed simply using sets

colors = {'red', 'green', 'red', 'blue', 'green', 'red', 'violet'}
print(type(colors))
print(len(colors))
print('red' in colors)
print('orange' in colors)

cool = {'green', 'blue', 'indigo', 'violet'}
print(colors.union(cool))
print(colors.intersection(cool))
print(colors.difference(cool))             # Differencing is not commutative
print(cool.difference(colors))

print(colors | cool)   # "or"  union
print(colors & cool)   # "and" intersection
print(colors - cool)   # "minus" difference

# My recommendation:  Use "-", "union", and "intersection".
#                     Don't use "|", "&", "difference".

print(set('abracadabrasimsalabim'))

################################################################
## Getting data from the interwebs

from urllib.request import urlopen

with urlopen('http://www.perl.org') as f:
    page = f.read().decode()

print(page[:500])

################################################################
## Lists literals are made with square brackets and commas
## Lists can also be made with the list() constructor
## Lists are ordered, indexable, iterable, dense, variant, arrays
## that allow duplicates.
## They are your most common data holder.
## They have many talents, but mostly we use them for looping.

states = ['texas', 'iowa', 'ohio', 'iowa', 'utah']
print(len(states))
print(states[0])
print([state.title() for state in states])
states.append('hawaii')
print(states)
print(states.pop())         # LIFO stack:  Removes and returns rightmost element (undoes an append)
states.insert(0, 'alaska')  # Don't do this.  It moves ALL the data to the right and does not scale well.
print(states)
print(states.sort())        # Typically None is returned to indicate mutated data
print(states)
print(states.reverse())
print(states)

print([states[0], states[1], states[2]])  # First three states
print(states[0 : 3])                      # Slicing

try:
    print(states[6])
except IndexError:
    print("Oops, I did it again. I indexed too far. I'm not that innocent.")

states = ['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
print(states[5])               # 1st state from the right    
print(states[6 - 1])
print(states[len(states) - 1])
print(states[-1])              # negative numbers add in len(), count from the right
print(states[-2])

print([states[-3], states[-2], states[-1]])  # last three states
print(states[-3 : ])           # omitted stop point goes to the end
print(states[ : -3])           # omitted start point starts at beginning

mo_states = ['new york', 'new jersey', 'new mexico']
for state in mo_states:
    states.append(state)       # can only add one state at a time
print(states)

states.append(mo_states)       # can only add one thing at a time
print(states)

states.extend(mo_states)       # will do the loop and append
print(states)

################################################################
## Getting data from disk

with open('data/hamlet.txt', encoding='utf-8') as f:
    play = f.read()

print(len(play))
print(play[:500])
