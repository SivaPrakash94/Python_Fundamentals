Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# C C++ Go
'interpreted' == 'compiled'
False
# Same category:  Perl Ruby TCL/Oop
# Variables are different.
# Assignments are different.
print('hello world')
hello world
len('hello')
5
# Learn to drive the IDE
n = 10
n ** 2
100
import os
os.getcwd()
'/Users/raymond/Dropbox/Public/sj257'
# Windows people, save your files here, this week.
# Don't create a new directory.  Put your stuff here.

# Interactive Shell Window    >>> |
print('goodbye cruel world')
goodbye cruel world

n ** 3 - 2 * x
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    n ** 3 - 2 * x
NameError: name 'x' is not defined
n ** 3 - 2 * n
980

# Windows:  Alt-P  Alt-N           Prev / Next
# Mac:      Cntl-P  Cntl-N         Prev / Next
os.listdir('.')
['overview.py', 'mtg_link.py', 'getting_setup.py', 'data', 'day1.py']

# Three ways to use previous lines:
#  * mouse, click, return
#  * arrow keys and return
#  * prev/next   alt/cntl

[x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[x**2 for x in range(10) if x%2==0]
[0, 4, 16, 36, 64]
[x**2 for x in range(-10, 11) if x%2==0]
[100, 64, 36, 16, 4, 0, 4, 16, 36, 64, 100]
{x**2 for x in range(-10, 11) if x%2==0}
{64, 0, 100, 4, 36, 16}

# Lists are ordered and allow duplicates
# Sets are unorded and eliminate duplicates

# x ** 2    means square of x
# range(-10, 11)   means   integers  in   -10 <= x < 11
list(range(-10, 11))
[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[x**2 for x in range(-10, 11)]
[100, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x % 2     remainder after dividing by 2
38 / 5
7.6
38 // 5
7
38 % 5
3
3 + 5 == 8
True
3 + 5 == 11
False
x = 38
x % 2
0
x % 2 == 0
True
[x**2 for x in range(-10, 11) if x%2==0]  # Make  a list of squares of x where x comes from -10 <= x < 11 but only if x is even
[100, 64, 36, 16, 4, 0, 4, 16, 36, 64, 100]
{x**2 for x in range(-10, 11) if x%2==0}
{64, 0, 100, 4, 36, 16}
{x**2 for x in range(-10, 11) if x%2==0}  # Make  a set of squares of x where x comes from -10 <= x < 11 but only if x is even
{64, 0, 100, 4, 36, 16}

= RESTART: /Users/raymond/Dropbox/Public/sj257/welcome_script.py
 Wow, it moves to the right!
  Wow, it moves to the right!
   Wow, it moves to the right!
    Wow, it moves to the right!
     Wow, it moves to the right!
      Wow, it moves to the right!
       Wow, it moves to the right!
        Wow, it moves to the right!
         Wow, it moves to the right!
          Wow, it moves to the right!
Done. Fini.  But not Kaput.
n
10
pad_char
' '
pad
'         '
i
9
type(n)
<class 'int'>
help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.


= RESTART: /Users/raymond/Dropbox/Public/sj257/welcome_script.py
 Wow, it moves to the right!
  Wow, it moves to the right!
   Wow, it moves to the right!
    Wow, it moves to the right!
     Wow, it moves to the right!
      Wow, it moves to the right!
       Wow, it moves to the right!
        Wow, it moves to the right!
         Wow, it moves to the right!
          Wow, it moves to the right!
           Wow, it moves to the right!
            Wow, it moves to the right!
Done. Fini.  But not Kaput.

= RESTART: /Users/raymond/Dropbox/Public/sj257/welcome_script.py
 Wow, it moves to the right!
. Wow, it moves to the right!
.. Wow, it moves to the right!
... Wow, it moves to the right!
.... Wow, it moves to the right!
..... Wow, it moves to the right!
...... Wow, it moves to the right!
....... Wow, it moves to the right!
........ Wow, it moves to the right!
......... Wow, it moves to the right!
.......... Wow, it moves to the right!
........... Wow, it moves to the right!
Done. Fini.  But not Kaput.

= RESTART: /Users/raymond/Dropbox/Public/sj257/welcome_script.py
 Wow, it moves to the right!!!
. Wow, it moves to the right!!!
.. Wow, it moves to the right!!!
... Wow, it moves to the right!!!
.... Wow, it moves to the right!!!
..... Wow, it moves to the right!!!
...... Wow, it moves to the right!!!
....... Wow, it moves to the right!!!
........ Wow, it moves to the right!!!
......... Wow, it moves to the right!!!
.......... Wow, it moves to the right!!!
........... Wow, it moves to the right!!!
Done. Fini.  But not Kaput.

= RESTART: /Users/raymond/Dropbox/Public/sj257/welcome_script.py
 Wow, it moves to the right!!!
_ Wow, it moves to the right!!!
__ Wow, it moves to the right!!!
___ Wow, it moves to the right!!!
____ Wow, it moves to the right!!!
Done. Fini.  But not Kaput.
pad
'____'
type(pad)
<class 'str'>
import os
os.chdir('data')

= RESTART: /Users/raymond/Dropbox/Public/sj257/welcome_script.py
 Wow, it moves to the right!!!
_ Wow, it moves to the right!!!
__ Wow, it moves to the right!!!
___ Wow, it moves to the right!!!
____ Wow, it moves to the right!!!
Done. Fini.  But not Kaput.
import os
os.getcwd()
'/Users/raymond/Dropbox/Public/sj257'
'l10O'
'l10O'

= RESTART: /Users/raymond/Dropbox/Public/sj257/welcome_script.py
 Wow, it moves to the right!!!
_ Wow, it moves to the right!!!
__ Wow, it moves to the right!!!
___ Wow, it moves to the right!!!
____ Wow, it moves to the right!!!
Done. Fini.  But not Kaput.

= RESTART: /Users/raymond/Dropbox/Public/sj257/welcome_script.py
 Wow, it moves to the right!!!
_ Wow, it moves to the right!!!
__ Wow, it moves to the right!!!
___ Wow, it moves to the right!!!
____ Wow, it moves to the right!!!
Done. Fini.  But not Kaput.

= RESTART: /Users/raymond/Dropbox/Public/sj257/overview.py
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/overview.py", line 23, in <module>
    visited = frequent_urls('data/*.log')
  File "/Users/raymond/Dropbox/Public/sj257/overview.py", line 11, in frequent_urls
    visited = collections.Counter()
NameError: name 'collections' is not defined

= RESTART: /Users/raymond/Dropbox/Public/sj257/overview.py
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/overview.py", line 23, in <module>
    visited = frequent_urls('data/*.log')
  File "/Users/raymond/Dropbox/Public/sj257/overview.py", line 11, in frequent_urls
    visited = colletions.Counter()
NameError: name 'colletions' is not defined. Did you mean: 'collections'?
Counter
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    Counter
NameError: name 'Counter' is not defined


import collections
collections
<module 'collections' from '/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/collections/__init__.py'>
collections.Counter
<class 'collections.Counter'>


raymond = 'red'
raymond = 'orange'

raymond
'orange'
# In ONE namespace, you can ONLY use a SINGLE name to refer to one thing at time.


instructor = 'red'
comedian = 'orange'

instructor
'red'
comedian
'orange'

====================== RESTART: Shell =====================
hettinger = {'raymond': 'red', 'rachel': 'blue'}
romano = {'raymond': 'orange', 'debra': 'green'}

hettinger['raymond']
'red'
romano['raymond']
'orange'
# hettingers.raymond

import math
pi
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
math.pi
3.141592653589793
import random
randrange
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    randrange
NameError: name 'randrange' is not defined
random.randrange(1000)
59
random.randrange(1000)
719
random.randrange(1000)
12


from types import SimpleNamespace
hettinger = SimpleNamespace(raymond='red', rachel='blue')
hettinger.rachel
'blue'


import random
import overview

# Standard library.   Third-party packages.   Ones you write.
dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# Python truth:  functions and classes are basically the same thing.  Python thinks of a class as a function that makes instances.

# Human truth:  we think of functions and classes as being very different.


# Brandon   Maxima   Nissan   Sedan  Reliable   PoorFuelEconomy    Blue     HalfTank
# Raymond   Maxima   Nissan   Sedan  Reliable   PoorFuelEconomy    Red      Three-quarters

class Maxima:
    make = 'Nissan'
    body = 'Sedan'
    reliable = True
    economy = 3

    
brandon = Maxima()
raymond = Maxima()


Maxima
<class '__main__.Maxima'>
type(brandon)
<class '__main__.Maxima'>
brandon
<__main__.Maxima object at 0x101acda20>
raymond
<__main__.Maxima object at 0x1021c3970>
Maxima, raymond, brandon
(<class '__main__.Maxima'>, <__main__.Maxima object at 0x1021c3970>, <__main__.Maxima object at 0x101acda20>)
brandon.color = 'Blue'
raymond.color = 'Red'
brandon.gas = 0.5
raymond.gas = 0.75

vars(brandon)
{'color': 'Blue', 'gas': 0.5}
vars(raymond)
{'color': 'Red', 'gas': 0.75}

brandon.color
'Blue'
raymond.color
'Red'
brandon.make
'Nissan'
raymond.make
'Nissan'

# Classes are like functions that make instances when you call them.
# Classes have an internal dictionary to store SHARED information
# Instances have an internal dictionary to store UNIQUE information
# Instances also know that their class is (so they can get to the shared information)

vars(raymond)
{'color': 'Red', 'gas': 0.75}
type(raymond)
<class '__main__.Maxima'>

vars(brandon)
{'color': 'Blue', 'gas': 0.5}
type(raymond)
<class '__main__.Maxima'>


brandon.color
'Blue'
brandon.make
'Nissan'
# If a function is moved inside a class, we call it a method.
# The ONLY thing special about method is that the instance is automatically filled-in as the first argument

class Maxima:
    make = 'Nissan'
    body = 'Sedan'
    reliable = True
    economy = 3
    def add_gas(inst, amount):
        inst.gas += amount

        
brandon = Maxima()
brandon.color = 'Blue'
brandon.gas = 0.5

brandon.add_gas(0.3)
vars(brandon)
{'color': 'Blue', 'gas': 0.8}
class Maxima:
    make = 'Nissan'
    body = 'Sedan'
    reliable = True
    economy = 3
    def add_gas(self, amount):
        self.gas += amount

        
import collections
person = collections.Counter()
country = collections.Counter()


person['raymond'] += 1
person['uk'] += 1

person['raymond'] += 1
person['de'] += 1

person['rachel'] += 1
person['uk'] += 1


person
Counter({'raymond': 2, 'uk': 2, 'de': 1, 'rachel': 1})



person = collections.Counter()
country = collections.Counter()
person['raymond'] += 1
country['uk'] += 1
person['raymond'] += 1
country['de'] += 1
person['rachel'] += 1
country['uk'] += 1


person
Counter({'raymond': 2, 'rachel': 1})
country
Counter({'uk': 2, 'de': 1})

person.most_common(1)
[('raymond', 2)]
Counter('abracadabara').most_common(3)
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    Counter('abracadabara').most_common(3)
NameError: name 'Counter' is not defined. Did you mean: 'country'?
collections.Counter('abracadabara').most_common(3)
[('a', 6), ('b', 2), ('r', 2)]
import math
math.cos(3.0)
-0.9899924966004454
import glob
type(glob)
<class 'module'>
glob.glob
<function glob at 0x1022241f0>
glob.glob('*.py')      # Globbing
['overview.py', 'mtg_link.py', 'welcome_script.py', 'getting_setup.py', 'day1.py']
# glob.glob   -> os.expand_wildcards('*.py')

# new york, new york
dir(glob)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_dir_open_flags', '_glob0', '_glob1', '_glob2', '_iglob', '_isdir', '_ishidden', '_isrecursive', '_iterdir', '_join', '_lexists', '_listdir', '_rlistdir', 'contextlib', 'escape', 'fnmatch', 'glob', 'glob0', 'glob1', 'has_magic', 'iglob', 'itertools', 'magic_check', 'magic_check_bytes', 'os', 're', 'stat', 'sys']
for s in glob.glob('*.py'):
    print(s)

    
overview.py
mtg_link.py
welcome_script.py
getting_setup.py
day1.py
for filename in glob.glob('*.py'):
    print(filename)

    
overview.py
mtg_link.py
welcome_script.py
getting_setup.py
day1.py
for filename in glob.glob('*.py'):
    print(filename.upper())

    
OVERVIEW.PY
MTG_LINK.PY
WELCOME_SCRIPT.PY
GETTING_SETUP.PY
DAY1.PY

# with-statements run setup and teardown logic
# threading.Lock       ^-- acquire  ^-- release
# open                     open         close
# db.connection        begin trx        rollback / commit


# Iterable means "for-able" or "loop-overable"
#   Iterable:  list  file

colors = ['red', 'green', 'blue']
for color in colors:
    print(color.upper())

    
RED
GREEN
BLUE
type(colors)
<class 'list'>
f = open('data/stocks.txt')
for line in f:
    print(line, len(line))

    
CSCO,100,18.04
 15
ANTM,200,45.03
 15
CSCO,150,19.05
 15
MSFT,250,80.56
 15
IBM,500,22.01
 14
ANTM,250,44.23
 15
GOOG,200,501.45
 16
CSCO,175,19.56
 15
MSFT,75,80.81
 14
GOOG,300,502.65
 16
IBM,150,25.01
 14

= RESTART: /Users/raymond/Dropbox/Public/sj257/overview.py =
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/overview.py", line 23, in <module>
    visited = frequent_urls('data/*.log')
  File "/Users/raymond/Dropbox/Public/sj257/overview.py", line 15, in frequent_urls
    mo = re.search(r'GET\s+(\S+)\s+200', line)
NameError: name 're' is not defined
import re

search
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    search
NameError: name 'search' is not defined
re.search
<function search at 0x100713400>
line = 'bettong.client.uq.oz.au -       807256884       GET     /history/skylab/skylab.html     200     1687'
mo = re.search(r'GET\s+(\S+)\s+200', line)
type(mo)
<class 're.Match'>
mo.span()
(48, 91)
mo.group(0)
'GET     /history/skylab/skylab.html     200'
mo.group(1)
'/history/skylab/skylab.html'
r'GET\s+(\S+)\s+200' == 'GET\\s+(\\S+)\\s+200'
True
colors = ['red', 'green', 'blue']


type(colors)
<class 'list'>
len(colors)
3
colors[0]
'red'
colors[1]
'green'
colors[2]
'blue'
colors[0].upper()
'RED'
colors[1].upper()
'GREEN'
'red'.upper()
'RED'
for x in colors:
    print(x)

    
red
green
blue
for color in colors:
    print(color)

    
red
green
blue
for color in colors:
    print(color.upper())

    
RED
GREEN
BLUE


# Different classes may have similar operations and dissimilar operations.


30 + 40
70
type(30)
<class 'int'>
'hello' + ' world'
'hello world'

30 * 40
1200
'hello' * 3
'hellohellohello'

30 ** 40
121576654590569288010000000000000000000000000000000000000000
'hello' ** 3
Traceback (most recent call last):
  File "<pyshell#294>", line 1, in <module>
    'hello' ** 3
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'


# Some classes can be looped over: iteration support
# Some classes are useable with the with-statement:  context manager support

# The support is added by methods with an interesting name pattern:  dunder name        double underscore

x = 30
x + 40
70
x.__add__(30)
60

x = 'hello'
x + ' world'
'hello world'
x.__add__(' world')
'hello world'

x = None
x + ' world'
Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    x + ' world'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'


# Some classes can be looped over: iteration support           __iter__
# Some classes are useable with the with-statement:  context manager support    __enter__  __exit__




============================================ RESTART: Shell ============================================
# Python is a fully object oriented language.
# Everything in Python is an object
# Object: str int dict list functions classes exceptions file
# Objects are encapsulated.  The ONLY way to interact with an object is throught its methods.

# Do we HAVE TO use "with"?  or HAVE TO use "for"?  HAVE TO use "+"   HAVE TO use "print".
#       GET TO                  GET TO              GET TO            GET TO


# No, you don't HAVE TO do anything, you could just use methods.
# Yes, you GET TO use nices approachs that call methods for you.


= RESTART: /Users/raymond/Dropbox/Public/sj257/why_dunder_methods.py
3 RED
5 GREEN
4 BLUE

= RESTART: /Users/raymond/Dropbox/Public/sj257/why_dunder_methods.py
3 RED
5 GREEN
4 BLUE
3 RED
5 GREEN
4 BLUE

dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
30 + 40
70
(30).__add__(40)
70
dir(None)
['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
None + None
Traceback (most recent call last):
  File "<pyshell#336>", line 1, in <module>
    None + None
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'


40 - 30
10
40 + 30
70

(40).__sub__(30)
10
(40).__add__(30)
70

'hello' + ' world'
'hello world'
'hello' - 'lo'
Traceback (most recent call last):
  File "<pyshell#345>", line 1, in <module>
    'hello' - 'lo'
TypeError: unsupported operand type(s) for -: 'str' and 'str'


dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
38 % 5
3
(38).__mod__(5)
3

'the answer is %d today' % 42
'the answer is 42 today'
'the answer is %d today'.__mod__(42)
'the answer is 42 today'
colors = ['red', 'green', 'blue']

'green' in colors
True
colors.__contains__('green')
True


colors
['red', 'green', 'blue']
colors[2]
'blue'
colors.__getitem__(2)
'blue'
pow(2, 5)
32
pow.__call__(2, 5)
32
colors[2]
'blue'

d = dict(raymond='red', rachel='blue')
d['rachel']
'blue'
d['rachel']
'blue'
d.__getitem__('rachel')
'blue'
class A:
    pass

a = A()
len(a)
Traceback (most recent call last):
  File "<pyshell#376>", line 1, in <module>
    len(a)
TypeError: object of type 'A' has no len()

class A:
    def __len__(self):
        return 99

    
a = A()
len(a)
99
divmod(38, 5)
(7, 3)
# Gazinta
(38).__divmod__(5)
(7, 3)


# A function inside a class (shared by all instances)
# is called a method().

# The ONLY thing special about a method
# is the instance is automatically put in the 1st argument.
A.__len__
<function A.__len__ at 0x103bf4430>
class A:
    def __len__(self):
        return 99

    
class B:
    def __len__(self):
        return 11

    
a = A()
b = B()
a.__len__()
99
b.__len__()
11


# Placehold object mean "no value at all"

x = 0      # This IS a value that less that 1
x = None

# None NULL null Om


a = Noe
Traceback (most recent call last):
  File "<pyshell#411>", line 1, in <module>
    a = Noe
NameError: name 'Noe' is not defined. Did you mean: 'None'?


a = None
SyntaxError: unexpected indent



a = None
b = None

a == b
True
a is b        # None is a singleton
True

a = 'raymond'
b = 'ray'
b += 'mond'

a == b
True
a is b
False
hex(id(a))
'0x103bcde30'
hex(id(b))
'0x1031c5270'
# Are strings singletons?
# Can you reliable use IS on two strings?  No.


s = 'hello'
len(s)              # Function
5
s.__len__()         # Method
5


#1) The default __name__ of a module is the string '__main__'
#2) Importing a module changes __name__.


= RESTART: /Users/raymond/Dropbox/Public/sj257/overview.py =
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]




r = range(10, 15)
s = ['manny', 'mo', 'jack']
d = {'raymond': 'red', 'rachel': 'blue'}

a = iter(r)
b = iter(s)
c = iter(d)

r
range(10, 15)
s
['manny', 'mo', 'jack']
d
{'raymond': 'red', 'rachel': 'blue'}

a
<range_iterator object at 0x10389b840>
b
<list_iterator object at 0x103681a20>
d
{'raymond': 'red', 'rachel': 'blue'}
c
<dict_keyiterator object at 0x102a32e30>

next(a)
10
next(a)
11
next(a)
12
next(s)
Traceback (most recent call last):
  File "<pyshell#468>", line 1, in <module>
    next(s)
TypeError: 'list' object is not an iterator
next(b)
'manny'
next(b)
'mo'

next(c)
'raymond'
next(c)
'rachel'
next(c)
Traceback (most recent call last):
  File "<pyshell#474>", line 1, in <module>
    next(c)
StopIteration

next(a)
13
next(a)
14
next(a)
Traceback (most recent call last):
  File "<pyshell#478>", line 1, in <module>
    next(a)
StopIteration

next(b)
'jack'
next(b)
Traceback (most recent call last):
  File "<pyshell#481>", line 1, in <module>
    next(b)
StopIteration
d
{'raymond': 'red', 'rachel': 'blue'}



= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
__name__
'__main__'
# dunder -> double underscore
dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
__name__
'__main__'
__file__
'/Users/raymond/Dropbox/Public/sj257/details.py'
__doc__
" A tour around the language.\nWe'll visit every part but not\nlinger too long.  That will save\ntime for the fun, writing applications.\n"
# ^-- "repper" representation repr()
# Show quotation marks.  Escapes control chars.
# Tries to show on one line.
# Ideally, it should "round-trip"
__doc__
" A tour around the language.\nWe'll visit every part but not\nlinger too long.  That will save\ntime for the fun, writing applications.\n"
" A tour around the language.\nWe'll visit every part but not\nlinger too long.  That will save\ntime for the fun, writing applications.\n" == __doc__
True
# Ideally, it should "round-trip"
# The output can recreate the string.

print(__doc__)
 A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.

# ^-- "stir" string str
# No quotes.  Control characters are executed.
# It shows on as many lines as needed.
# It looks pretty.

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
print(__doc__)
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
print(__doc__)
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.



= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.
import details
Name of the module details
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


My name changed, so I WAS imported

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.
<class 'dict'>

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.
<class 'dict'>
5

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/details.py", line 47, in <module>
    print(kind['target'])
KeyError: 'target'

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
import random
print(random.__doc__)
Random variable generators.

    bytes
    -----
           uniform bytes (values between 0 and 255)

    integers
    --------
           uniform within range

    sequences
    ---------
           pick random element
           pick random sample
           pick weighted random sample
           generate random permutation

    distributions on the real line:
    ------------------------------
           uniform
           triangular
           normal (Gaussian)
           lognormal
           negative exponential
           gamma
           beta
           pareto
           Weibull

    distributions on the circle (angles 0 to 2pi)
    ---------------------------------------------
           circular uniform
           von Mises

General notes on the underlying Mersenne Twister core generator:

* The period is 2**19937-1.
* It is one of the most extensively tested generators in existence.
* The random() method is implemented in C, executes in a single Python step,
  and is, therefore, threadsafe.



= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
# Cost will matter:  O(1)  O(n)  O(log n)   O(n log n)
# Costs that won't matter in this calls
# Costs that won't matter in this class
#    Tiny performance differences between two ways of doing things


= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business



color = {'raymond': 'red', 'rachel': 'blue'}
color.get('rachel', 'black')
'blue'
color.get('cindy', 'black')
'black'

def myget(mapping, key, default):
    try:
        return mapping[key]
    except KeyError:
        raise default

    
myget(color, 'rachel', 'black')
'blue'
myget(color, 'cindy', 'black')
Traceback (most recent call last):
  File "<pyshell#527>", line 3, in myget
    return mapping[key]
KeyError: 'cindy'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#529>", line 1, in <module>
    myget(color, 'cindy', 'black')
  File "<pyshell#527>", line 5, in myget
    raise default
TypeError: exceptions must derive from BaseException
def myget(mapping, key, default):
    try:
        return mapping[key]
    except KeyError:
        return default

    



def myget(mapping, key, default):
    try:
        return mapping[key]
    except KeyError:
        return default

    
myget(color, 'cindy', 'black')
'black'

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business


xyz = 10
abc123 = 20
123abc = 30        # Identifiers must start with A-Za-z_
SyntaxError: invalid decimal literal
raymond hettinger = 40  # Identifiers must A-Za-z_0-9
SyntaxError: invalid syntax

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
k2
{'cisco': 'networking', 'sysco': 'food service'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
-0.9899924966004454
1.252762968495368
3268760
11861676288000

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
-0.9899924966004454
1.252762968495368
3268760
11861676288000
18525

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
-0.9899924966004454
1.252762968495368
3268760
11861676288000
15697
13901
1_34_5678_6
13456786
13456786
13456786
# DO HAVE TO -> DO GET TO
1_234_456
1234456
1_234_456 == 1234456
True

= RESTART: /Users/raymond/Dropbox/Public/sj257/overview.py
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]

= RESTART: /Users/raymond/Dropbox/Public/sj257/overview_terrible.py
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]

= RESTART: /Users/raymond/Dropbox/Public/sj257/overview.py
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
-0.9899924966004454
1.252762968495368
3268760
11861676288000
11434
14684
[('s', 2), ('i', 2), ('m', 2)]

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
-0.9899924966004454
1.252762968495368
3268760
11861676288000
11571
14331
[('s', 2), ('i', 2), ('m', 2)]
70

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
-0.9899924966004454
1.252762968495368
3268760
11861676288000
14876
18164
[('s', 2), ('i', 2), ('m', 2)]
70
1728
12 ** 3
1728

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
-0.9899924966004454
1.252762968495368
3268760
11861676288000
15519
18030
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
# Do you HAVE TO use functions?

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
-0.9899924966004454
1.252762968495368
3268760
11861676288000
11159
17262
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
-0.9899924966004454
1.252762968495368
3268760
11861676288000
14341
10931
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
cube.__call__(4)
64
type(cube)
<class 'function'>
dir(cube)
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
-0.9899924966004454
1.252762968495368
3268760
11861676288000
16834
18864
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
-0.9899924966004454
1.252762968495368
3268760
11861676288000
19200
17684
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
-0.9899924966004454
1.252762968495368
3268760
11861676288000
18730
19136
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[82, 101, 100, 32, 98, 117, 108, 108, 32, 104, 97, 115, 32, 119, 105, 105, 105, 110, 103, 115]

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
10509
16252
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[82, 101, 100, 32, 98, 117, 108, 108, 32, 104, 97, 115, 32, 119, 105, 105, 105, 110, 103, 115]

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
14558
14398
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']


__name__
'__main__'
__doc__
"A tour around the language.\nWe'll visit every part but not\nlinger too long.  That will save\ntime for the fun, writing applications.\n"

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
12417
16206
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.


= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
17529
19838
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
11500
13952
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: None

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.


======== RESTART: /Users/raymond/Dropbox/Public/sj257/details.py ========
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
19217
15219
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

help(ord)
Help on built-in function ord in module builtins:

ord(c, /)
    Return the Unicode code point for a one-character string.

help(cube)
Help on function cube in module __main__:

cube(x)
    Return a value times itself thrice.

help(math.comb)
Help on built-in function comb in module math:

comb(n, k, /)
    Number of ways to choose k items from n items without repetition and without order.
    
    Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
    to zero when k > n.
    
    Also called the binomial coefficient because it is equivalent
    to the coefficient of k-th term in polynomial expansion of the
    expression (1 + x)**n.
    
    Raises TypeError if either of the arguments are not integers.
    Raises ValueError if either of the arguments are negative.






# Endo -- inside   Exo -- outside
# Nyn -- name

# Endonym what people or countries call themselves.
# Exo:  China    Endo:  The Central State
# Exo:  Greece   Endo:  Hello
# Exo:  Finland  Endo:  Land
# Exo:  Spain  Aleman   Endo:  Espana

lambda x: x ** 3
<function <lambda> at 0x10567fd90>
(lambda x: x ** 3)(5)
125

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
10412
14894
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
13045
19944
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
19937
13780
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
colors
{'green', 'blue', 'violet', 'red'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
16458
14744
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
colors
{'red', 'blue', 'violet', 'green'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
12896
18603
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
19637
17674
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'red', 'violet', 'green', 'indigo', 'blue'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
14182
12404
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'blue', 'violet', 'red', 'indigo'}
{'violet', 'green', 'blue'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
14411
11996
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'blue', 'violet', 'green', 'indigo', 'red'}
{'green', 'blue', 'violet'}
{'red'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
10706
19352
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'red', 'green', 'indigo', 'violet', 'blue'}
{'blue', 'green', 'violet'}
{'red'}
{'indigo'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
14873
10367
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'red', 'indigo', 'blue', 'violet'}
{'violet', 'blue', 'green'}
{'red'}
{'indigo'}
{'green', 'red', 'indigo', 'blue', 'violet'}
{'violet', 'blue', 'green'}
{'red'}
natural = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
even = {2, 4, 6, 8, 10}
prime = {2, 3, 5, 7, 11}

even <= natural
True
prime <= natural
True
odd = natural - even
odd
{1, 3, 5, 7, 9, 11}
prime - odd
{2}
prime & odd
{11, 3, 5, 7}
prime | even
{2, 3, 4, 5, 6, 7, 8, 10, 11}
natural - (prime | even)
{1, 9}


# main   failover

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
15755
14339
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'violet', 'green', 'blue', 'red', 'indigo'}
{'violet', 'green', 'blue'}
{'red'}
{'indigo'}
{'violet', 'green', 'blue', 'red', 'indigo'}
{'violet', 'green', 'blue'}
{'red'}
{'d', 's', 'c', 'a', 'i', 'm', 'r', 'b', 'l'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
16624
11357
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'red', 'violet', 'indigo', 'blue'}
{'blue', 'violet', 'green'}
{'red'}
{'indigo'}
{'green', 'red', 'violet', 'indigo', 'blue'}
{'blue', 'violet', 'green'}
{'red'}
{'a', 's', 'r', 'c', 'l', 'i', 'b', 'd', 'm'}
type(pages)
Traceback (most recent call last):
  File "<pyshell#595>", line 1, in <module>
    type(pages)
NameError: name 'pages' is not defined. Did you mean: 'page'?
type(page)
<class 'bytes'>
#  something you can use --(encode)--> storething you can store or transmit

========= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py =========
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
11462
13146
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'red', 'violet', 'indigo', 'blue'}
{'green', 'blue', 'violet'}
{'red'}
{'indigo'}
{'green', 'red', 'violet', 'indigo', 'blue'}
{'green', 'blue', 'violet'}
{'red'}
{'m', 'l', 'r', 'b', 'd', 'i', 'c', 'a', 's'}
type(page)
<class 'str'>

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
17376
12936
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'indigo', 'blue', 'red', 'violet'}
{'green', 'violet', 'blue'}
{'red'}
{'indigo'}
{'green', 'indigo', 'blue', 'red', 'violet'}
{'green', 'violet', 'blue'}
{'red'}
{'i', 'a', 'b', 'd', 'r', 's', 'c', 'm', 'l'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *af

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
14898
11259
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'violet', 'red', 'blue', 'indigo', 'green'}
{'violet', 'blue', 'green'}
{'red'}
{'indigo'}
{'violet', 'red', 'blue', 'indigo', 'green'}
{'violet', 'blue', 'green'}
{'red'}
{'i', 'r', 'a', 'b', 'm', 'd', 'l', 'c', 's'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=

===================================================== RESTART: Shell =====================================================
import math              # We learn ONE new word: math
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'math']
math
<module 'math' from '/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload/math.cpython-310-darwin.so'>
math.pi
3.141592653589793
math.cos(3.0)
-0.9899924966004454

cos(3.0)
Traceback (most recent call last):
  File "<pyshell#605>", line 1, in <module>
    cos(3.0)
NameError: name 'cos' is not defined

===================================================== RESTART: Shell =====================================================
# How to do math in Python
import math
math.cos(3.0 * math.pi * math.sqrt(3.5)) + math.sin(3.0 * math.pi * math.sqrt(4.5))
1.2561312628345147

cos = math.cos
sin = math.sin
pi = math.pi
sqrt = math.sqrt
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'cos', 'math', 'pi', 'sin', 'sqrt']

cos(3.0 * pi * sqrt(3.5)) + sin(3.0 * pi * sqrt(4.5))
1.2561312628345147

===================================================== RESTART: Shell =====================================================
from math import cos, pi, sqrt, sin
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'cos', 'pi', 'sin', 'sqrt']
cos(3.0 * pi * sqrt(3.5)) + sin(3.0 * pi * sqrt(4.5))
1.2561312628345147


# Google:  Never use from imports.
# If you use something many times or are finding the dot be distracting use a from-import.
# If you want to emphasize where something came from, use a regular import
#           re.search(pattern, line)


===================================================== RESTART: Shell =====================================================
c= 12.5
d = 14.3
e = 17.6
f = 18.2

alpha = 0.25
beta = 0.76
gamma = 0.97

from math import *
log(c)
2.5257286443082556
log(d)
2.6602595372658615
log(e)
1.0
log(f)
2.9014215940827497

c
12.5
d
14.3
e
2.718281828459045
f
18.2
exp(alpha)
1.2840254166877414
exp(beta)
2.1382762204968184
exp(gamma)
Traceback (most recent call last):
  File "<pyshell#648>", line 1, in <module>
    exp(gamma)
TypeError: must be real number, not builtin_function_or_method
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'alpha', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'beta', 'c', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'd', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'f', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


'could ya' == 'should ya'
False


# double temperature[20];
s = [10, 20, 30.5, 'thirty', None, {'a': 1}]
len(s)
6
s[0] + 1
11
s[2] + 2.5
33.0
s[3] + 0.75
Traceback (most recent call last):
  File "<pyshell#660>", line 1, in <module>
    s[3] + 0.75
TypeError: can only concatenate str (not "float") to str
s[1] + 2.5
22.5
s[2] + 2.5
33.0
s[3].upper()
'THIRTY'
type(s[4])
<class 'NoneType'>
s[5]['a']
1




= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
18220
15506
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'red', 'green', 'blue', 'indigo', 'violet'}
{'green', 'blue', 'violet'}
{'red'}
{'indigo'}
{'red', 'green', 'blue', 'indigo', 'violet'}
{'green', 'blue', 'violet'}
{'red'}
{'a', 'b', 'i', 'r', 's', 'c', 'd', 'm', 'l'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
13829
13160
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'red', 'violet', 'blue', 'green', 'indigo'}
{'green', 'blue', 'violet'}
{'red'}
{'indigo'}
{'red', 'violet', 'blue', 'green', 'indigo'}
{'green', 'blue', 'violet'}
{'red'}
{'i', 'a', 'c', 'm', 'b', 'd', 'r', 'l', 's'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
13820
17488
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'violet', 'indigo', 'blue', 'red', 'green'}
{'violet', 'green', 'blue'}
{'red'}
{'indigo'}
{'violet', 'indigo', 'blue', 'red', 'green'}
{'violet', 'green', 'blue'}
{'red'}
{'s', 'i', 'a', 'c', 'r', 'm', 'l', 'b', 'd'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['TEXAS', 'IOWA', 'OHIO', 'IOWA', 'UTAH']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
17244
15525
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'red', 'blue', 'indigo', 'violet', 'green'}
{'blue', 'violet', 'green'}
{'red'}
{'indigo'}
{'red', 'blue', 'indigo', 'violet', 'green'}
{'blue', 'violet', 'green'}
{'red'}
{'b', 'a', 'm', 'l', 'd', 'r', 'c', 'i', 's'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
15509
18499
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'red', 'green', 'indigo', 'violet', 'blue'}
{'green', 'blue', 'violet'}
{'red'}
{'indigo'}
{'red', 'green', 'indigo', 'violet', 'blue'}
{'green', 'blue', 'violet'}
{'red'}
{'d', 's', 'a', 'r', 'l', 'c', 'm', 'b', 'i'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
10878
11174
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'indigo', 'blue', 'green', 'red', 'violet'}
{'green', 'blue', 'violet'}
{'red'}
{'indigo'}
{'indigo', 'blue', 'green', 'red', 'violet'}
{'green', 'blue', 'violet'}
{'red'}
{'m', 'd', 'i', 'a', 'b', 'l', 'c', 's', 'r'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
states
['texas', 'iowa', 'ohio', 'iowa', 'utah']
# Ghost Fleet!


= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
11802
16716
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'indigo', 'green', 'blue', 'violet', 'red'}
{'blue', 'violet', 'green'}
{'red'}
{'indigo'}
{'indigo', 'green', 'blue', 'violet', 'red'}
{'blue', 'violet', 'green'}
{'red'}
{'m', 's', 'b', 'r', 'd', 'a', 'c', 'i', 'l'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
13985
17341
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'blue', 'violet', 'indigo', 'red'}
{'green', 'blue', 'violet'}
{'red'}
{'indigo'}
{'green', 'blue', 'violet', 'indigo', 'red'}
{'green', 'blue', 'violet'}
{'red'}
{'b', 'm', 'i', 'c', 'l', 'r', 'a', 'd', 's'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
13270
16266
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'violet', 'indigo', 'red', 'blue', 'green'}
{'green', 'violet', 'blue'}
{'red'}
{'indigo'}
{'violet', 'indigo', 'red', 'blue', 'green'}
{'green', 'violet', 'blue'}
{'red'}
{'b', 'd', 'm', 'c', 'i', 'a', 'l', 'r', 's'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
14934
14130
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'red', 'violet', 'blue', 'indigo'}
{'blue', 'green', 'violet'}
{'red'}
{'indigo'}
{'green', 'red', 'violet', 'blue', 'indigo'}
{'blue', 'green', 'violet'}
{'red'}
{'c', 'a', 'd', 's', 'i', 'b', 'm', 'r', 'l'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
17516
18933
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'blue', 'violet', 'indigo', 'red', 'green'}
{'violet', 'green', 'blue'}
{'red'}
{'indigo'}
{'blue', 'violet', 'indigo', 'red', 'green'}
{'violet', 'green', 'blue'}
{'red'}
{'b', 'm', 'l', 'd', 'a', 's', 'r', 'i', 'c'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
15600
18121
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'blue', 'violet', 'red', 'indigo', 'green'}
{'blue', 'green', 'violet'}
{'red'}
{'indigo'}
{'blue', 'violet', 'red', 'indigo', 'green'}
{'blue', 'green', 'violet'}
{'red'}
{'d', 'a', 'i', 'b', 'm', 'r', 's', 'l', 'c'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
12390
15552
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'violet', 'red', 'blue', 'indigo'}
{'blue', 'green', 'violet'}
{'red'}
{'indigo'}
{'green', 'violet', 'red', 'blue', 'indigo'}
{'blue', 'green', 'violet'}
{'red'}
{'l', 'r', 'c', 's', 'd', 'a', 'm', 'b', 'i'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
12719
13648
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'indigo', 'blue', 'red', 'green', 'violet'}
{'green', 'violet', 'blue'}
{'red'}
{'indigo'}
{'indigo', 'blue', 'red', 'green', 'violet'}
{'green', 'violet', 'blue'}
{'red'}
{'r', 'i', 'a', 'b', 'm', 's', 'l', 'c', 'd'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
13445
15536
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'indigo', 'violet', 'blue', 'green', 'red'}
{'violet', 'green', 'blue'}
{'red'}
{'indigo'}
{'indigo', 'violet', 'blue', 'green', 'red'}
{'violet', 'green', 'blue'}
{'red'}
{'b', 'a', 'm', 's', 'd', 'r', 'i', 'l', 'c'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/details.py", line 204, in <module>
    print(states[6])
IndexError: list index out of range

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
11074
16367
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'red', 'violet', 'blue', 'green', 'indigo'}
{'blue', 'violet', 'green'}
{'red'}
{'indigo'}
{'red', 'violet', 'blue', 'green', 'indigo'}
{'blue', 'violet', 'green'}
{'red'}
{'d', 's', 'a', 'm', 'c', 'r', 'i', 'b', 'l'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
14957
10717
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'blue', 'violet', 'indigo', 'red', 'green'}
{'blue', 'green', 'violet'}
{'red'}
{'indigo'}
{'blue', 'violet', 'indigo', 'red', 'green'}
{'blue', 'green', 'violet'}
{'red'}
{'r', 'c', 'i', 's', 'm', 'a', 'l', 'd', 'b'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
17473
15295
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'blue', 'violet', 'green', 'indigo', 'red'}
{'green', 'blue', 'violet'}
{'red'}
{'indigo'}
{'blue', 'violet', 'green', 'indigo', 'red'}
{'green', 'blue', 'violet'}
{'red'}
{'m', 'b', 'a', 's', 'd', 'l', 'c', 'i', 'r'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
16668
12668
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'indigo', 'blue', 'violet', 'red', 'green'}
{'green', 'violet', 'blue'}
{'red'}
{'indigo'}
{'indigo', 'blue', 'violet', 'red', 'green'}
{'green', 'violet', 'blue'}
{'red'}
{'c', 'l', 's', 'r', 'd', 'i', 'm', 'b', 'a'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
12600
16640
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'indigo', 'red', 'blue', 'violet', 'green'}
{'green', 'blue', 'violet'}
{'red'}
{'indigo'}
{'indigo', 'red', 'blue', 'violet', 'green'}
{'green', 'blue', 'violet'}
{'red'}
{'s', 'r', 'b', 'c', 'd', 'i', 'm', 'a', 'l'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
17151
15207
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'red', 'blue', 'violet', 'indigo'}
{'blue', 'green', 'violet'}
{'red'}
{'indigo'}
{'green', 'red', 'blue', 'violet', 'indigo'}
{'blue', 'green', 'violet'}
{'red'}
{'m', 'd', 'a', 'l', 'r', 'b', 'c', 'i', 's'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska
alaska

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
10026
17699
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'violet', 'indigo', 'blue', 'green', 'red'}
{'green', 'violet', 'blue'}
{'red'}
{'indigo'}
{'violet', 'indigo', 'blue', 'green', 'red'}
{'green', 'violet', 'blue'}
{'red'}
{'c', 'a', 'b', 'r', 'd', 'i', 'l', 'm', 's'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska
alaska
alaska
iowa

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
12958
10540
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'red', 'green', 'blue', 'violet', 'indigo'}
{'blue', 'green', 'violet'}
{'red'}
{'indigo'}
{'red', 'green', 'blue', 'violet', 'indigo'}
{'blue', 'green', 'violet'}
{'red'}
{'c', 'd', 'l', 'm', 'a', 's', 'i', 'b', 'r'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska
alaska
alaska
iowa
['iowa', 'iowa', 'alaska']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
19389
10585
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'violet', 'red', 'blue', 'indigo'}
{'green', 'blue', 'violet'}
{'red'}
{'indigo'}
{'green', 'violet', 'red', 'blue', 'indigo'}
{'green', 'blue', 'violet'}
{'red'}
{'r', 'l', 's', 'c', 'm', 'b', 'a', 'd', 'i'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska
alaska
alaska
iowa
['iowa', 'iowa', 'alaska']
['iowa', 'iowa', 'alaska']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
14896
13533
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'red', 'indigo', 'green', 'violet', 'blue'}
{'green', 'violet', 'blue'}
{'red'}
{'indigo'}
{'red', 'indigo', 'green', 'violet', 'blue'}
{'green', 'violet', 'blue'}
{'red'}
{'r', 'd', 's', 'm', 'c', 'a', 'i', 'l', 'b'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska
alaska
alaska
iowa
['iowa', 'iowa', 'alaska']
['iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
len(range(10))
10
len(range(20, 30))          # start <= i < stop
10
list(range(20, 40, 2))      # start, stop, step
[20, 22, 24, 26, 28, 30, 32, 34, 36, 38]

=================================== RESTART: /Users/raymond/Dropbox/Public/sj257/details.py ==================================
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
15791
18648
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'violet', 'green', 'red', 'indigo', 'blue'}
{'violet', 'blue', 'green'}
{'red'}
{'indigo'}
{'violet', 'green', 'red', 'indigo', 'blue'}
{'violet', 'blue', 'green'}
{'red'}
{'s', 'a', 'c', 'r', 'd', 'l', 'm', 'i', 'b'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska
alaska
alaska
iowa
['iowa', 'iowa', 'alaska']
['iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']

=================================== RESTART: /Users/raymond/Dropbox/Public/sj257/details.py ==================================
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
11491
17534
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'red', 'green', 'blue', 'violet', 'indigo'}
{'blue', 'violet', 'green'}
{'red'}
{'indigo'}
{'red', 'green', 'blue', 'violet', 'indigo'}
{'blue', 'violet', 'green'}
{'red'}
{'a', 'r', 'm', 'd', 'l', 'i', 'c', 's', 'b'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska
alaska
alaska
iowa
['iowa', 'iowa', 'alaska']
['iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska', 'new york', 'new jersey', 'new mexico']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
15928
13320
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'green', 'indigo', 'blue', 'violet', 'red'}
{'blue', 'green', 'violet'}
{'red'}
{'indigo'}
{'green', 'indigo', 'blue', 'violet', 'red'}
{'blue', 'green', 'violet'}
{'red'}
{'b', 'm', 'i', 'd', 'l', 's', 'r', 'a', 'c'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska
alaska
alaska
iowa
['iowa', 'iowa', 'alaska']
['iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska', 'new york', 'new jersey', 'new mexico']

= RESTART: /Users/raymond/Dropbox/Public/sj257/details.py
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
11282
15665
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'indigo', 'green', 'blue', 'red', 'violet'}
{'green', 'blue', 'violet'}
{'red'}
{'indigo'}
{'indigo', 'green', 'blue', 'red', 'violet'}
{'green', 'blue', 'violet'}
{'red'}
{'b', 's', 'r', 'm', 'l', 'd', 'a', 'i', 'c'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska
alaska
alaska
iowa
['iowa', 'iowa', 'alaska']
['iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska', 'new york', 'new jersey', 'new mexico']
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska', 'new york', 'new jersey', 'new mexico', ['new york', 'new jersey', 'new mexico']]

=================================== RESTART: /Users/raymond/Dropbox/Public/sj257/details.py ==================================
Name of the module __main__
Filename: /Users/raymond/Dropbox/Public/sj257/details.py
Docstring:
A tour around the language.
We'll visit every part but not
linger too long.  That will save
time for the fun, writing applications.


I have the default name, so I was NOT imported.

<class 'dict'>
5
True
networking
dict_keys(['cisco', 'crisco', 'costco', 'sysco', 'san franscisco'])
dict_values(['networking', 'shortening', 'retail', 'food service', 'municipality'])
dict_items([('cisco', 'networking'), ('crisco', 'shortening'), ('costco', 'retail'), ('sysco', 'food service'), ('san franscisco', 'municipality')])
target is in an unknown business
target is in an unknown business
target is in the unknown business
{'cisco': 'networking', 'sysco': 'food service', 'san_franscisco': 'municipality'}
65
A
0x64
-0.9899924966004454
1.252762968495368
3268760
11861676288000
16668
11638
[('s', 2), ('i', 2), ('m', 2)]
70
1728
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
['0x52', '0x65', '0x64', '0x20', '0x62', '0x75', '0x6c', '0x6c', '0x20', '0x68', '0x61', '0x73', '0x20', '0x77', '0x69', '0x69', '0x69', '0x6e', '0x67', '0x73']
Name: cube
Module: __main__
Docstring: Return a value times itself thrice.

Name: introspect
Module: __main__
Docstring: Look inside a function to find the name, module, and doc

Name: ord
Module: builtins
Docstring: Return the Unicode code point for a one-character string.

Name: comb
Module: math
Docstring: Number of ways to choose k items from n items without repetition and without order.

Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
to zero when k > n.

Also called the binomial coefficient because it is equivalent
to the coefficient of k-th term in polynomial expansion of the
expression (1 + x)**n.

Raises TypeError if either of the arguments are not integers.
Raises ValueError if either of the arguments are negative.

[4, -38, -80, -92, -44, 94, 352, 760, 1348, 2146]
<class 'set'>
4
True
False
{'indigo', 'green', 'blue', 'violet', 'red'}
{'green', 'violet', 'blue'}
{'red'}
{'indigo'}
{'indigo', 'green', 'blue', 'violet', 'red'}
{'green', 'violet', 'blue'}
{'red'}
{'m', 's', 'l', 'i', 'c', 'd', 'b', 'a', 'r'}


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="The Perl Programming Language at Perl.org. Links and other helpful resources for new and experienced Perl programmers." />
    
    <link rel=
5
texas
['Texas', 'Iowa', 'Ohio', 'Iowa', 'Utah']
['texas', 'iowa', 'ohio', 'iowa', 'utah', 'hawaii']
hawaii
['alaska', 'texas', 'iowa', 'ohio', 'iowa', 'utah']
None
['alaska', 'iowa', 'iowa', 'ohio', 'texas', 'utah']
None
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio']
Oops, I did it again. I indexed too far. I'm not that innocent.
alaska
alaska
alaska
alaska
iowa
['iowa', 'iowa', 'alaska']
['iowa', 'iowa', 'alaska']
['utah', 'texas', 'ohio']
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska', 'new york', 'new jersey', 'new mexico']
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska', 'new york', 'new jersey', 'new mexico', ['new york', 'new jersey', 'new mexico']]
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska', 'new york', 'new jersey', 'new mexico', ['new york', 'new jersey', 'new mexico'], 'new york', 'new jersey', 'new mexico']

names = ['bob', 'tom', 'alice']
names += 'becky'
names
['bob', 'tom', 'alice', 'b', 'e', 'c', 'k', 'y']
names += ['becky']
names
['bob', 'tom', 'alice', 'b', 'e', 'c', 'k', 'y', 'becky']
names.append('becky')


s = []
names = ['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
for name in names:
    s = s + [name]

    
s
['utah', 'texas', 'ohio', 'iowa', 'iowa', 'alaska']
s = []
for name in names:
    s = s + [name.upper()]

    
s
['UTAH', 'TEXAS', 'OHIO', 'IOWA', 'IOWA', 'ALASKA']


s = []
name = 'utah'
s + ['utah']
['utah']
s = s + ['utah']
name = 'texas'
s + [name]
['utah', 'texas']
s = s + [name]
name = 'ohio'
s + [name]
['utah', 'texas', 'ohio']

s
['utah', 'texas']
s = s + [name]


s = []
for name in names:
    s.append(name.title())

    
s
['Utah', 'Texas', 'Ohio', 'Iowa', 'Iowa', 'Alaska']

# + makes new lists


x = 10
y = 5
x + y
15
x
10
y
5
x = x + y

# Easy:  Go to Dropbox.  Find the "data" folder".  Click on Download.
# Usually goes to Downloads.   Click on it to unzip it.
# Sometimes hard:  Move that whole folder to be a subdirectory of you current directory.
import os
os.getcwd()
'/Users/raymond/Dropbox/Public/sj257'
# Verify it worked
os.listdir('data')
['re.txt', 'tmp.txt', 'bh_canon.html', '2011shannonphd.pdf', 'books.xml', 'stocks.txt', 'vcard.html', 'ipv4_int_bri.txt~', 'raisin_team.csv', 'magicmethods.pdf', 'team_history.txt', 'books.json', 'word.txt', 'raisin_team_update.csv', 'team_history.json', 'ftd_interfaces.txt', 'ipv4_int_bri.txt', 'vcard.css', 'CSRRESTAPI.pdf', 'url.txt', 'mtg_link.txt', 'show_team_history.py', 'PythonAwesome.pdf', 'parse_demo2.txt', 'fsm.py', 'nasa_19950801.log', 'team_history.yaml', 'hamlet.txt', 'parse_demo1.txt']

# Set a timer and do EXACTLY 15 minutes of review.  Time box you study.
# Bring written questions tomorrow:   I don't understand the += on line 15 of overview.py
# Aim is for mastery learning.  We want 95% mastery of everything so far.
# https://www.dropbox.com/sh/94zatfgqvay8jdf/AAB0OAWIW0lwrGnXy6zivTSGa?dl=0

# Mind hack:  The optimal time according the research is the half hour before bed.
