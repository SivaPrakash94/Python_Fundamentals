Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# https://www.dropbox.com/sh/94zatfgqvay8jdf/AAB0OAWIW0lwrGnXy6zivTSGa?dl=0
# 95% mastery

# The for-loop ALWAYS calls __iter__
# It ALWAYS makes an assignment from __next__.

# The iterable can be many things:
# file:line, list:element, tuple:elem, string:char

# A list can contain ANY object including other lists and tuples.

# Sequences like like lists and tuples can be unpacked
# during assignment.

person = ('tom', 'hanks', 62, 'captain ...')
fname, lname, age, movie = person

fname
'tom'
lname
'hanks'
age
62
movie
'captain ...'
person[0]
'tom'
person[1]
'hanks'
person[2]
62
s = [10, 20, 30]
for x in s:
    print(type(x), x, x**2)

    
<class 'int'> 10 100
<class 'int'> 20 400
<class 'int'> 30 900

lot = [(10, 'ten'), (20, 'twenty'), (30, 'thirty')]
len(lot)
3
lot[0]
(10, 'ten')
lot[1]
(20, 'twenty')
lot[2]
(30, 'thirty')
it = iter(lot)
next(it)
(10, 'ten')
next(it)
(20, 'twenty')
next(it)
(30, 'thirty')
next(it)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    next(it)
StopIteration


for t in lot:
    print(t)

    
(10, 'ten')
(20, 'twenty')
(30, 'thirty')
for t in lot:
    print(type(t), len(t), t[0], t[1], t)

    
<class 'tuple'> 2 10 ten (10, 'ten')
<class 'tuple'> 2 20 twenty (20, 'twenty')
<class 'tuple'> 2 30 thirty (30, 'thirty')
for t in lot:
    number, name = t
    print(name, '-->', number)

    
ten --> 10
twenty --> 20
thirty --> 30

t
(30, 'thirty')
number
30
name
'thirty'
for number, name in lot:
    print(name, '-->', number)

    
ten --> 10
twenty --> 20
thirty --> 30
lot
[(10, 'ten'), (20, 'twenty'), (30, 'thirty')]


lot
[(10, 'ten'), (20, 'twenty'), (30, 'thirty')]

it = enumerate(['zero', 'one', 'two'])
next(it)
(0, 'zero')
next(it)
(1, 'one')
next(it)
(2, 'two')
next(it)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    next(it)
StopIteration


for i, name in enumerate(['zero', 'one', 'two']):
    print(name, '-->', number)

    
zero --> 30
one --> 30
two --> 30


class A:
    def __len__(self):
        return 42
    def __getitem__(self, i):
        return i ** 2

    
class A:
    def __len__(self):
        return 42
    def __getitem__(self, i):
        return i ** 2
    def __call__(self, x, y):
        return x + y
    def __repr__(self):
        return 'some repper'

    
a = A()
a.__len__()
42
a.__getitem__(15)
225
a.__call__(5, 25)
30
a.__repr__()
'some repper'

len(a)
42
a[15]
225
a(5, 25)
30
a
some repper

# The dunder short-cuts are built-into the interpreter.
# They are given.  You don't get to invent new ones.
# []    always calls __getitem__


dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

d = {'raymond': 'red'}
d.__getitem__('raymond')
'red'
d['raymond']
'red'
d('raymond')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    d('raymond')
TypeError: 'dict' object is not callable


class Dict(dict):
    def __call__(self, key):
        return self[key]

    
d = Dict(d)
d
{'raymond': 'red'}
d.keys()
dict_keys(['raymond'])
d.values()
dict_values(['red'])
d['raymond']
'red'
dir(d)
['__call__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
d['raymond']
'red'
d('raymond')
'red'

# If you get OOP and the shortcut-to-method mapping,
# all that is left is learning individual classes


s = 'the tale of two cities'
s.upper()
'THE TALE OF TWO CITIES'
type(s)
<class 'str'>
str.upper(s)
'THE TALE OF TWO CITIES'


# Top 50%   Core language and concepts
#           A bunch of simple, practical scripts

# Top 10%   Go through the standard library
#           Build bigger applications








class A:
    x = 10

    
a = A()
a.y = 20

vars(A)
mappingproxy({'__module__': '__main__', 'x': 10, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None})
vars(a)
{'y': 20}


a.x
10
a.y
20

def mygetattr(obj, attrname, default):
    try:
        return vars(obj)[attrname]
    except KeyError:
        pass
    try:
        return vars(type(obj))[attrname]
    except KeyError:
        return default

    
vars(a)['y']
20
a.y
20
mygetattr(a, 'y', 0)
20

vars(A)
mappingproxy({'__module__': '__main__', 'x': 10, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None})
vars(A)['x']
10
type(a) == A
True
vars(type(a))['x']
10
a.x
10
mygetattr(a, 'x', 0)
10


a.y
20
mygetattr(a, 'y', 0)     # vars(a)['y']
20

a.x
10
mygetattr(a, 'x', 0)     # vars(type(a))['x']
10

mygetattr(a, 'z', 0)
0
def mygetattr(obj, attrname, default):
    try:
        return vars(obj)[attrname]
    except KeyError:
        pass
    try:
        return vars(type(obj))[attrname]
    except KeyError:
        return default

    
getattr(a, 'x', 0)
10
getattr(a, 'y', 0)
20
getattr(a, 'z', 0)
0

v = 'x'
getattr(a, v, 0)
10


for name in ('x', 'y', 'z'):
    print(name, getattr(a, name, 0))

    
x 10
y 20
z 0





s = 'the tale of two cities'
s.upper()
'THE TALE OF TWO CITIES'
s.title()
'The Tale Of Two Cities'

case = 'upper'
s.case()
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    s.case()
AttributeError: 'str' object has no attribute 'case'



s = 'the tale of two cities'
case = 'upper'
getattr(s, case)()
'THE TALE OF TWO CITIES'
case = 'title'
getattr(s, case)()
'The Tale Of Two Cities'


from our_eval import myeval
s = '"hello" * 5'
tokens = s.split()
tokens
['"hello"', '*', '5']
p, op, q = tokens
p
'"hello"'
op
'*'
q
'5'
pv = myeval(p, ns)
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    pv = myeval(p, ns)
NameError: name 'ns' is not defined. Did you mean: 's'?
pv = myeval(p, {})
pv
'hello'
qv = myeval(q, {})
qv
5
q
'5'
qv
5


pv
'hello'
qv
5
op
'*'
method_name = operator_map[op]
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    method_name = operator_map[op]
NameError: name 'operator_map' is not defined
from our_eval import myeval, operator_map
method_name = operator_map[op]
method_name
'__mul__'


pv
'hello'
method_name
'__mul__'
qv
5
getattr(pv, method_name)(5)
'hellohellohellohellohello'
pv.__mul__(5)
'hellohellohellohellohello'


'hello'.__mul__(5)
'hellohellohellohellohello'
'hello' * 5
'hellohellohellohellohello'


pow(2, 5)
32

f = pow
f
<built-in function pow>
f(2, 5)
32


def g():
    return pow

g()
<built-in function pow>
g()(2, 5)
32

'hello'.__mul__(5)
'hellohellohellohellohello'

s = 'hello'
pv = 'hello'

pv.__mul__(5)
'hellohellohellohellohello'
(pv . __mul__)  (5)
'hellohellohellohellohello'
getattr(pv, '__mul__')  (5)
'hellohellohellohellohello'

30 + 40 - 5
65
(30 + 40) - 5
65
70 - 5
65


s = 'the tale of two cities'
s.replace('two', 'three')
'the tale of three cities'
s.replace
<built-in method replace of str object at 0x102b90710>
bm = s.replace
bm('two', 'three')
'the tale of three cities'


s . replace        ('two', 'three')
'the tale of three cities'
bm = s.replace
bm       ('two', 'three')
'the tale of three cities'

getattr(s, 'replace')        ('two', 'three')
'the tale of three cities'


method_name = 'replace'
getattr(s, method_name)('two', 'three')
'the tale of three cities'


s.replace('two', 'three')
'the tale of three cities'


pass       # Do nothing, nop STATEMENT
None       # A value that means nothing, EXPRESSION

pass
a = None
a = pass
SyntaxError: invalid syntax



a = pass
SyntaxError: invalid syntax
a = None


story = "x = 30 + 40"
varname = 'x'
expr = '30 + 40'
globals()[varname] = eval(expr)

x
70
story = "x := 30 + 40;"




if x = 20 : y = 5
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

# if x > 20 : y = 5
x > 20
True
x > 200
False
if x > 20 : y = 5

y
5
if x > 20 y = 5
SyntaxError: invalid syntax
if x > 20 : y = 5

if x > 20:
    y = 5
else:
    y = 10

    
if x > 20:
else:
    y = 10
    
SyntaxError: expected an indented block after 'if' statement on line 1

if x > 20:
    pass
else:
    y = 10

    

for i in range(10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
eval('range(10)')
range(0, 10)


for i in range(10):
    pass

for i in range(10):
    pass
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for i in range(10):
    print(i)
    if i == 5:
        print('five')
        continue
    print('---')

    
0
---
1
---
2
---
3
---
4
---
5
five
6
---
7
---
8
---
9
---
for i in range(10):
    print(i)
    if i == 5:
        print('five')
        continue
    if i == 8:
        break
    print('---')

    
0
---
1
---
2
---
3
---
4
---
5
five
6
---
7
---
8
import math
math
<module 'math' from '/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload/math.cpython-310-darwin.so'>


lot = [(10, 'ten'), (20, 'twenty'), (30, 'thirty')]
type(lot)
<class 'list'>
len(lot)
3
lot[0]
(10, 'ten')
lot[1]
(20, 'twenty')
lot[2]
(30, 'thirty')

for t in lot:
    print(t)

    
(10, 'ten')
(20, 'twenty')
(30, 'thirty')
it = lot.__iter__()
lot
[(10, 'ten'), (20, 'twenty'), (30, 'thirty')]
it
<list_iterator object at 0x1039d3c70>
it.__next__()
(10, 'ten')
t = it.__next__()
t
(20, 'twenty')

for sometuple in lot:
    print(sometuple)

    
(10, 'ten')
(20, 'twenty')
(30, 'thirty')
names = ['alice', 'bob', 'charles']
for name in names:
    print(name.upper())

    
ALICE
BOB
CHARLES
for moniker in names:
    print(moniker.upper())

    
ALICE
BOB
CHARLES
lot
[(10, 'ten'), (20, 'twenty'), (30, 'thirty')]
lot[0]
(10, 'ten')
names[0]
'alice'


for sometuple in lot:
    print(sometuple)

    
(10, 'ten')
(20, 'twenty')
(30, 'thirty')

sometuple
(30, 'thirty')
for sometuple in lot:
    number = sometuple[0]
    name = sometuple[1]

    
for sometuple in lot:
    number = sometuple[0]
    name = sometuple[1]
    print(name, number)

    
ten 10
twenty 20
thirty 30
sometuple
(30, 'thirty')
sometuple[0]
30
for sometuple in lot:
    number, name = sometuple[0]
    print(name, number)

    
Traceback (most recent call last):
  File "<pyshell#417>", line 2, in <module>
    number, name = sometuple[0]
TypeError: cannot unpack non-iterable int object
for sometuple in lot:
    number, name = sometuple
    print(name, number)

    
ten 10
twenty 20
thirty 30
for number, name in lot:
    print(name, number)

    
ten 10
twenty 20
thirty 30



= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash Works for a living
Raymond Hettinger Works for a living
Anna Sakharova Works for a living
type(raymond)
<class '__main__.Contractor'>
type(siva)
<class '__main__.Employee'>


vars(raymond)
{'name': 'Raymond Hettinger'}
vars(Contractor)
mappingproxy({'__module__': '__main__', 'status': 'Works for a living', 'serviced_company': 'Cisco', '__dict__': <attribute '__dict__' of 'Contractor' objects>, '__weakref__': <attribute '__weakref__' of 'Contractor' objects>, '__doc__': None})

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male Works for a living
Raymond Hettinger male Works for a living
Anna Sakharova female Works for a living


type(raymond)
<class '__main__.Contractor'>
vars(raymond)
{'name': 'Raymond Hettinger', 'gender': 'male'}
vars(Employee)
mappingproxy({'__module__': '__main__', 'status': 'Works for a living', 'location': 'San Jose', '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None})

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male Works for a living
Raymond Hettinger male Works for a living
Anna Sakharova female Works for a living

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Anna Sakharova female works for a living
Contractor.status
'works for a living'
Employee.status
'works for a living'

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Anna Sakharova female works for a living
Worker
<class '__main__.Worker'>
Contractor
<class '__main__.Contractor'>
initialize
<function initialize at 0x10176f6d0>
siva
<__main__.Employee object at 0x1017abf10>
anna
<__main__.Employee object at 0x1017abeb0>
raymond
<__main__.Contractor object at 0x1017ab700>
team
[<__main__.Employee object at 0x1017abf10>, <__main__.Contractor object at 0x1017ab700>, <__main__.Employee object at 0x1017abeb0>]


# HAS A  vs   IS A
anna.location
'San Jose'

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Anna Sakharova female works for a living
# Toronto:Eng     Montreal:Fr
# Commonweath     Ask QofE to choose
# c) Ottowa

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Anna Sakharova female works for a living
anna.location
'Ottawa'
siva.location
'San Jose'
Employee.location
'San Jose'


anna.location
'Ottawa'
siva.location
'San Jose'

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Anna Sakharova female works for a living
x = 10
x = 12

def square(x):
    return x ** 2

def square(x):
    return 'pointy circle'

square(5)
'pointy circle'

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/oop_demo.py", line 32, in <module>
    initialize_e('Anna Sakharova', 'female', 'Ottawa')
  File "/Users/raymond/Dropbox/Public/sj257/oop_demo.py", line 20, in initialize_e
    employee.name = name
AttributeError: 'str' object has no attribute 'name'

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Anna Sakharova female works for a living

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Anna Sakharova female works for a living


Employee.location
'San Jose'
Employee.initialize
<function Employee.initialize at 0x10522fc70>

Contractor.serviced_company
'Cisco'
Contractor.initialize
<function Contractor.initialize at 0x10522fbe0>


class Hettinger:
    raymond = 'red'
    rachel = 'blue'

    
class Romano:
    raymond = 'orange'
    debra = 'green'

    

vars(Hettinger)
mappingproxy({'__module__': '__main__', 'raymond': 'red', 'rachel': 'blue', '__dict__': <attribute '__dict__' of 'Hettinger' objects>, '__weakref__': <attribute '__weakref__' of 'Hettinger' objects>, '__doc__': None})
vars(Romano)
mappingproxy({'__module__': '__main__', 'raymond': 'orange', 'debra': 'green', '__dict__': <attribute '__dict__' of 'Romano' objects>, '__weakref__': <attribute '__weakref__' of 'Romano' objects>, '__doc__': None})


Hettinger.raymond
'red'
Romano.raymond
'orange'

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Anna Sakharova female works for a living

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/oop_demo.py", line 38, in <module>
    print(person.name, person.gender, person.status)
AttributeError: 'Contractor' object has no attribute 'name'
vars(raymond)
{'name': 'Raymond Hettinger', 'gender': 'male'}
vars(daniel)
{}

# Anytime you make an instance, you need to
# inititalize it (put the data in)
# or else it is useless.


= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Daniel Miz male works for a living
Anna Sakharova female works for a living

= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Daniel Miz male works for a living
Anna Sakharova female works for a living

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py =================================
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/oop_demo.py", line 25, in <module>
    raymond = Contractor('Raymond Hettinger', 'male')  # --> Contractor.initialize(raymond, 'Raymond Hettinger', 'male')
TypeError: Contractor.__init__() takes 2 positional arguments but 3 were given

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py =================================
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Daniel Miz male works for a living
Anna Sakharova female works for a living

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py =================================
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Daniel Miz male works for a living
Anna Sakharova female works for a living
print(raymond.show())
Traceback (most recent call last):
  File "<pyshell#499>", line 1, in <module>
    print(raymond.show())
  File "/Users/raymond/Dropbox/Public/sj257/oop_demo.py", line 16, in show
    return f'Contractor {self.name} is a {self.gender} servicing {self.service_company}'
AttributeError: 'Contractor' object has no attribute 'service_company'. Did you mean: 'serviced_company'?

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py =================================
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Daniel Miz male works for a living
Anna Sakharova female works for a living
print(raymond.show())
Contractor Raymond Hettinger is a male servicing Cisco

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py =================================
Siva Prakash male works for a living
Raymond Hettinger male works for a living
Daniel Miz male works for a living
Anna Sakharova female works for a living
print(siva.show())
Employee Siva Prakash is a male working from San Jose

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py =================================
Employee Siva Prakash is a male working from San Jose
Contractor Raymond Hettinger is a male servicing Cisco
Contractor Daniel Miz is a male servicing Cisco
Employee Anna Sakharova is a female working from Ottawa

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py =================================
Employee Siva Prakash is a male working from San Jose
Contractor Raymond Hettinger is a male servicing Cisco
Contractor Daniel Miz is a male servicing Cisco
Employee Anna Sakharova is a female working from Ottawa

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py =================================
Employee Siva Prakash is a male working from San Jose
Contractor Raymond Hettinger is a male servicing Cisco
Contractor Daniel Miz is a male servicing Cisco
Employee Anna Sakharova is a female working from Ottawa

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/oop_demo.py =================================
Employee Siva Prakash is a male working from San Jose
Contractor Raymond Hettinger is a male servicing Cisco
Contractor Daniel Miz is a male servicing Cisco
Employee Anna Sakharova is a female working from Ottawa
# Dunder methods CAN be called directly.
# But they almost always have nice looking short cuts

# print(obj)        -->  sys.stdout.write(obj.__str__)

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py
Interface                      IP-Address       Status            Protocol
Loopback0                      51.51.51.51      Up                Up
MgmtEth0/RSP0/CPU0/0           1.20.30.40       Up                Up
MgmtEth0/RSP0/CPU0/1           unassigned       Down              Down
MgmtEth0/RSP1/CPU0/0           unassigned       Up                Up
HundredGigE0/1/0/0             unassigned       Shutdown          Down
HundredGigE0/1/0/1             unassigned       Shutdown          Down
TenGigE0/2/0/0                 unassigned       Down              Down
TenGigE0/2/0/1                 unassigned       Down              Down
TenGigE0/2/0/2                 unassigned       Down              Down
TenGigE0/2/0/4                 unassigned       Down              Down
TenGigE0/2/0/5                 unassigned       Down              Down
TenGigE0/2/0/6                 unassigned       Down              Down
TenGigE0/2/0/7                 unassigned       Down              Down
GigabitEthernet0/3/0/1         unassigned       Up                Up
GigabitEthernet0/3/0/2         unassigned       Down              Down
GigabitEthernet0/3/0/3         unassigned       Up                Up
GigabitEthernet0/3/0/4         unassigned       Down              Down
GigabitEthernet0/3/0/5         unassigned       Down              Down
GigabitEthernet0/3/0/6         unassigned       Down              Down
GigabitEthernet0/3/0/7         unassigned       Down              Down
GigabitEthernet0/3/0/8         unassigned       Down              Down
GigabitEthernet0/3/0/9         unassigned       Down              Down
GigabitEthernet0/3/0/10        unassigned       Down              Down
GigabitEthernet0/3/0/11        unassigned       Down              Down
GigabitEthernet0/3/0/12        unassigned       Down              Down
GigabitEthernet0/3/0/13        unassigned       Down              Down
GigabitEthernet0/3/0/14        unassigned       Down              Down
GigabitEthernet0/3/0/15        unassigned       Down              Down
GigabitEthernet0/3/0/16        unassigned       Down              Down
GigabitEthernet0/3/0/17        unassigned       Down              Down
GigabitEthernet0/3/0/18        unassigned       Down              Down
GigabitEthernet0/3/0/19        unassigned       Down              Down
TenGigE0/3/1/0                 unassigned       Up                Up
TenGigE0/3/1/1                 unassigned       Down              Down
TenGigE0/3/1/2                 unassigned       Down              Down
TenGigE0/3/1/3                 unassigned       Up                Up
GigabitEthernet0/4/0/0         unassigned       Down              Down
TenGigE0/4/0/0                 unassigned       Up                Up
GigabitEthernet0/4/0/1         unassigned       Down              Down
TenGigE0/4/0/1                 unassigned       Down              Down
GigabitEthernet0/4/0/2         unassigned       Down              Down
GigabitEthernet0/4/0/3         unassigned       Down              Down
GigabitEthernet0/4/0/4         unassigned       Down              Down
GigabitEthernet0/4/0/5         unassigned       Down              Down
GigabitEthernet0/4/0/6         unassigned       Down              Down
GigabitEthernet0/4/0/7         unassigned       Down              Down
GigabitEthernet0/4/0/8         unassigned       Down              Down
GigabitEthernet0/4/0/9         unassigned       Down              Down
GigabitEthernet0/4/0/10        unassigned       Down              Down
GigabitEthernet0/4/0/11        unassigned       Down              Down
GigabitEthernet0/4/0/12        unassigned       Down              Down
GigabitEthernet0/4/0/13        unassigned       Down              Down
GigabitEthernet0/4/0/14        unassigned       Down              Down
GigabitEthernet0/4/0/15        unassigned       Down              Down
GigabitEthernet0/4/0/16        unassigned       Down              Down
GigabitEthernet0/4/0/17        unassigned       Down              Down
GigabitEthernet0/4/0/18        unassigned       Down              Down
GigabitEthernet0/4/0/19        unassigned       Down              Down
FortyGigE0/5/0/0               unassigned       Shutdown          Down
FortyGigE0/5/0/1               unassigned       Shutdown          Down
TenGigE0/5/1/0                 unassigned       Shutdown          Down
TenGigE0/5/1/1                 111.1.1.1        Up                Up
GigabitEthernet0/7/0/0         unassigned       Down              Down
GigabitEthernet0/7/0/1         unassigned       Down              Down
GigabitEthernet0/7/0/2         unassigned       Down              Down
GigabitEthernet0/7/0/3         unassigned       Down              Down
GigabitEthernet0/7/0/4         unassigned       Down              Down
GigabitEthernet0/7/0/5         unassigned       Down              Down
GigabitEthernet0/7/0/6         unassigned       Down              Down
GigabitEthernet0/7/0/7         unassigned       Down              Down
GigabitEthernet0/7/0/8         unassigned       Down              Down
GigabitEthernet0/7/0/9         unassigned       Down              Down
GigabitEthernet0/7/0/10        unassigned       Down              Down
GigabitEthernet0/7/0/11        unassigned       Down              Down
GigabitEthernet0/7/0/12        unassigned       Down              Down
GigabitEthernet0/7/0/13        unassigned       Down              Down
GigabitEthernet0/7/0/14        unassigned       Down              Down
GigabitEthernet 0/7/0/15       unassigned       Up
GigabitEthernet0/7/0/16        unassigned       Down              Down
GigabitEthernet0/7/0/17        unassigned       Down              Down
GigabitEthernet0/7/0/18        unassigned       Down              Down
GigabitEthernet0/7/0/19        unassigned       Down              Down
GigabitEthernet0/7/0/20        unassigned       Down              Down
GigabitEthernet0/7/0/21        unassigned       Down              Down
GigabitEthernet0/7/0/22        unassigned       Down              Down
GigabitEthernet0/7/0/23        unassigned       Down              Down
GigabitEthernet0/7/0/24        unassigned       Down              Down
GigabitEthernet0/7/0/25        unassigned       Down              Down
GigabitEthernet0/7/0/26        unassigned       Down              Down
GigabitEthernet0/7/0/27        unassigned       Down              Down
GigabitEthernet0/7/0/28        unassigned       Down              Down
GigabitEthernet0/7/0/29        unassigned       Down              Down
GigabitEthernet0/7/0/30        unassigned       Down              Down
GigabitEthernet0/7/0/31        unassigned       Down              Down
GigabitEthernet0/7/0/32        unassigned       Down              Down
GigabitEthernet0/7/0/33        unassigned       Down              Down
GigabitEthernet0/7/0/36        unassigned       Down              Down
GigabitEthernet0/7/0/37        unassigned       Down              Down
GigabitEthernet0/7/0/38        unassigned       Down              Down
GigabitEthernet0/7/0/39        unassigned       Down              Down


================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
Interface                      IP-Address       Status            Protocol

Loopback0                      51.51.51.51      Up                Up

MgmtEth0/RSP0/CPU0/0           1.20.30.40       Up                Up

MgmtEth0/RSP0/CPU0/1           unassigned       Down              Down

MgmtEth0/RSP1/CPU0/0           unassigned       Up                Up

HundredGigE0/1/0/0             unassigned       Shutdown          Down

HundredGigE0/1/0/1             unassigned       Shutdown          Down

TenGigE0/2/0/0                 unassigned       Down              Down

TenGigE0/2/0/1                 unassigned       Down              Down

TenGigE0/2/0/2                 unassigned       Down              Down

TenGigE0/2/0/4                 unassigned       Down              Down

TenGigE0/2/0/5                 unassigned       Down              Down

TenGigE0/2/0/6                 unassigned       Down              Down

TenGigE0/2/0/7                 unassigned       Down              Down

GigabitEthernet0/3/0/1         unassigned       Up                Up

GigabitEthernet0/3/0/2         unassigned       Down              Down

GigabitEthernet0/3/0/3         unassigned       Up                Up

GigabitEthernet0/3/0/4         unassigned       Down              Down

GigabitEthernet0/3/0/5         unassigned       Down              Down

GigabitEthernet0/3/0/6         unassigned       Down              Down

GigabitEthernet0/3/0/7         unassigned       Down              Down

GigabitEthernet0/3/0/8         unassigned       Down              Down

GigabitEthernet0/3/0/9         unassigned       Down              Down

GigabitEthernet0/3/0/10        unassigned       Down              Down

GigabitEthernet0/3/0/11        unassigned       Down              Down

GigabitEthernet0/3/0/12        unassigned       Down              Down

GigabitEthernet0/3/0/13        unassigned       Down              Down

GigabitEthernet0/3/0/14        unassigned       Down              Down

GigabitEthernet0/3/0/15        unassigned       Down              Down

GigabitEthernet0/3/0/16        unassigned       Down              Down

GigabitEthernet0/3/0/17        unassigned       Down              Down

GigabitEthernet0/3/0/18        unassigned       Down              Down

GigabitEthernet0/3/0/19        unassigned       Down              Down

TenGigE0/3/1/0                 unassigned       Up                Up

TenGigE0/3/1/1                 unassigned       Down              Down

TenGigE0/3/1/2                 unassigned       Down              Down

TenGigE0/3/1/3                 unassigned       Up                Up

GigabitEthernet0/4/0/0         unassigned       Down              Down

TenGigE0/4/0/0                 unassigned       Up                Up

GigabitEthernet0/4/0/1         unassigned       Down              Down

TenGigE0/4/0/1                 unassigned       Down              Down

GigabitEthernet0/4/0/2         unassigned       Down              Down

GigabitEthernet0/4/0/3         unassigned       Down              Down

GigabitEthernet0/4/0/4         unassigned       Down              Down

GigabitEthernet0/4/0/5         unassigned       Down              Down

GigabitEthernet0/4/0/6         unassigned       Down              Down

GigabitEthernet0/4/0/7         unassigned       Down              Down

GigabitEthernet0/4/0/8         unassigned       Down              Down

GigabitEthernet0/4/0/9         unassigned       Down              Down

GigabitEthernet0/4/0/10        unassigned       Down              Down

GigabitEthernet0/4/0/11        unassigned       Down              Down

GigabitEthernet0/4/0/12        unassigned       Down              Down

GigabitEthernet0/4/0/13        unassigned       Down              Down

GigabitEthernet0/4/0/14        unassigned       Down              Down

GigabitEthernet0/4/0/15        unassigned       Down              Down

GigabitEthernet0/4/0/16        unassigned       Down              Down

GigabitEthernet0/4/0/17        unassigned       Down              Down

GigabitEthernet0/4/0/18        unassigned       Down              Down

GigabitEthernet0/4/0/19        unassigned       Down              Down

FortyGigE0/5/0/0               unassigned       Shutdown          Down

FortyGigE0/5/0/1               unassigned       Shutdown          Down

TenGigE0/5/1/0                 unassigned       Shutdown          Down

TenGigE0/5/1/1                 111.1.1.1        Up                Up

GigabitEthernet0/7/0/0         unassigned       Down              Down

GigabitEthernet0/7/0/1         unassigned       Down              Down

GigabitEthernet0/7/0/2         unassigned       Down              Down

GigabitEthernet0/7/0/3         unassigned       Down              Down

GigabitEthernet0/7/0/4         unassigned       Down              Down

GigabitEthernet0/7/0/5         unassigned       Down              Down

GigabitEthernet0/7/0/6         unassigned       Down              Down

GigabitEthernet0/7/0/7         unassigned       Down              Down

GigabitEthernet0/7/0/8         unassigned       Down              Down

GigabitEthernet0/7/0/9         unassigned       Down              Down

GigabitEthernet0/7/0/10        unassigned       Down              Down

GigabitEthernet0/7/0/11        unassigned       Down              Down

GigabitEthernet0/7/0/12        unassigned       Down              Down

GigabitEthernet0/7/0/13        unassigned       Down              Down

GigabitEthernet0/7/0/14        unassigned       Down              Down

GigabitEthernet 0/7/0/15       unassigned       Up

GigabitEthernet0/7/0/16        unassigned       Down              Down

GigabitEthernet0/7/0/17        unassigned       Down              Down

GigabitEthernet0/7/0/18        unassigned       Down              Down

GigabitEthernet0/7/0/19        unassigned       Down              Down

GigabitEthernet0/7/0/20        unassigned       Down              Down

GigabitEthernet0/7/0/21        unassigned       Down              Down

GigabitEthernet0/7/0/22        unassigned       Down              Down

GigabitEthernet0/7/0/23        unassigned       Down              Down

GigabitEthernet0/7/0/24        unassigned       Down              Down

GigabitEthernet0/7/0/25        unassigned       Down              Down

GigabitEthernet0/7/0/26        unassigned       Down              Down

GigabitEthernet0/7/0/27        unassigned       Down              Down

GigabitEthernet0/7/0/28        unassigned       Down              Down

GigabitEthernet0/7/0/29        unassigned       Down              Down

GigabitEthernet0/7/0/30        unassigned       Down              Down

GigabitEthernet0/7/0/31        unassigned       Down              Down

GigabitEthernet0/7/0/32        unassigned       Down              Down

GigabitEthernet0/7/0/33        unassigned       Down              Down

GigabitEthernet0/7/0/36        unassigned       Down              Down

GigabitEthernet0/7/0/37        unassigned       Down              Down

GigabitEthernet0/7/0/38        unassigned       Down              Down

GigabitEthernet0/7/0/39        unassigned       Down              Down

interface
'GigabitEthernet0/7/0/39        unassigned       Down              Down\n'

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
['Interface', 'IP-Address', 'Status', 'Protocol']
['Loopback0', '51.51.51.51', 'Up', 'Up']
['MgmtEth0/RSP0/CPU0/0', '1.20.30.40', 'Up', 'Up']
['MgmtEth0/RSP0/CPU0/1', 'unassigned', 'Down', 'Down']
['MgmtEth0/RSP1/CPU0/0', 'unassigned', 'Up', 'Up']
['HundredGigE0/1/0/0', 'unassigned', 'Shutdown', 'Down']
['HundredGigE0/1/0/1', 'unassigned', 'Shutdown', 'Down']
['TenGigE0/2/0/0', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/1', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/2', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/4', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/5', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/6', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/7', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/1', 'unassigned', 'Up', 'Up']
['GigabitEthernet0/3/0/2', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/3', 'unassigned', 'Up', 'Up']
['GigabitEthernet0/3/0/4', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/5', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/6', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/7', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/8', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/9', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/10', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/11', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/12', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/13', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/14', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/15', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/16', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/17', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/18', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/19', 'unassigned', 'Down', 'Down']
['TenGigE0/3/1/0', 'unassigned', 'Up', 'Up']
['TenGigE0/3/1/1', 'unassigned', 'Down', 'Down']
['TenGigE0/3/1/2', 'unassigned', 'Down', 'Down']
['TenGigE0/3/1/3', 'unassigned', 'Up', 'Up']
['GigabitEthernet0/4/0/0', 'unassigned', 'Down', 'Down']
['TenGigE0/4/0/0', 'unassigned', 'Up', 'Up']
['GigabitEthernet0/4/0/1', 'unassigned', 'Down', 'Down']
['TenGigE0/4/0/1', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/2', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/3', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/4', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/5', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/6', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/7', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/8', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/9', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/10', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/11', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/12', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/13', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/14', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/15', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/16', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/17', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/18', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/19', 'unassigned', 'Down', 'Down']
['FortyGigE0/5/0/0', 'unassigned', 'Shutdown', 'Down']
['FortyGigE0/5/0/1', 'unassigned', 'Shutdown', 'Down']
['TenGigE0/5/1/0', 'unassigned', 'Shutdown', 'Down']
['TenGigE0/5/1/1', '111.1.1.1', 'Up', 'Up']
['GigabitEthernet0/7/0/0', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/1', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/2', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/3', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/4', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/5', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/6', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/7', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/8', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/9', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/10', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/11', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/12', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/13', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/14', 'unassigned', 'Down', 'Down']
['GigabitEthernet', '0/7/0/15', 'unassigned', 'Up']
['GigabitEthernet0/7/0/16', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/17', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/18', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/19', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/20', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/21', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/22', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/23', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/24', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/25', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/26', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/27', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/28', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/29', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/30', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/31', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/32', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/33', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/36', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/37', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/38', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/39', 'unassigned', 'Down', 'Down']

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
IP-Address Interface
51.51.51.51 Loopback0
1.20.30.40 MgmtEth0/RSP0/CPU0/0
unassigned MgmtEth0/RSP0/CPU0/1
unassigned MgmtEth0/RSP1/CPU0/0
unassigned HundredGigE0/1/0/0
unassigned HundredGigE0/1/0/1
unassigned TenGigE0/2/0/0
unassigned TenGigE0/2/0/1
unassigned TenGigE0/2/0/2
unassigned TenGigE0/2/0/4
unassigned TenGigE0/2/0/5
unassigned TenGigE0/2/0/6
unassigned TenGigE0/2/0/7
unassigned GigabitEthernet0/3/0/1
unassigned GigabitEthernet0/3/0/2
unassigned GigabitEthernet0/3/0/3
unassigned GigabitEthernet0/3/0/4
unassigned GigabitEthernet0/3/0/5
unassigned GigabitEthernet0/3/0/6
unassigned GigabitEthernet0/3/0/7
unassigned GigabitEthernet0/3/0/8
unassigned GigabitEthernet0/3/0/9
unassigned GigabitEthernet0/3/0/10
unassigned GigabitEthernet0/3/0/11
unassigned GigabitEthernet0/3/0/12
unassigned GigabitEthernet0/3/0/13
unassigned GigabitEthernet0/3/0/14
unassigned GigabitEthernet0/3/0/15
unassigned GigabitEthernet0/3/0/16
unassigned GigabitEthernet0/3/0/17
unassigned GigabitEthernet0/3/0/18
unassigned GigabitEthernet0/3/0/19
unassigned TenGigE0/3/1/0
unassigned TenGigE0/3/1/1
unassigned TenGigE0/3/1/2
unassigned TenGigE0/3/1/3
unassigned GigabitEthernet0/4/0/0
unassigned TenGigE0/4/0/0
unassigned GigabitEthernet0/4/0/1
unassigned TenGigE0/4/0/1
unassigned GigabitEthernet0/4/0/2
unassigned GigabitEthernet0/4/0/3
unassigned GigabitEthernet0/4/0/4
unassigned GigabitEthernet0/4/0/5
unassigned GigabitEthernet0/4/0/6
unassigned GigabitEthernet0/4/0/7
unassigned GigabitEthernet0/4/0/8
unassigned GigabitEthernet0/4/0/9
unassigned GigabitEthernet0/4/0/10
unassigned GigabitEthernet0/4/0/11
unassigned GigabitEthernet0/4/0/12
unassigned GigabitEthernet0/4/0/13
unassigned GigabitEthernet0/4/0/14
unassigned GigabitEthernet0/4/0/15
unassigned GigabitEthernet0/4/0/16
unassigned GigabitEthernet0/4/0/17
unassigned GigabitEthernet0/4/0/18
unassigned GigabitEthernet0/4/0/19
unassigned FortyGigE0/5/0/0
unassigned FortyGigE0/5/0/1
unassigned TenGigE0/5/1/0
111.1.1.1 TenGigE0/5/1/1
unassigned GigabitEthernet0/7/0/0
unassigned GigabitEthernet0/7/0/1
unassigned GigabitEthernet0/7/0/2
unassigned GigabitEthernet0/7/0/3
unassigned GigabitEthernet0/7/0/4
unassigned GigabitEthernet0/7/0/5
unassigned GigabitEthernet0/7/0/6
unassigned GigabitEthernet0/7/0/7
unassigned GigabitEthernet0/7/0/8
unassigned GigabitEthernet0/7/0/9
unassigned GigabitEthernet0/7/0/10
unassigned GigabitEthernet0/7/0/11
unassigned GigabitEthernet0/7/0/12
unassigned GigabitEthernet0/7/0/13
unassigned GigabitEthernet0/7/0/14
0/7/0/15 GigabitEthernet
unassigned GigabitEthernet0/7/0/16
unassigned GigabitEthernet0/7/0/17
unassigned GigabitEthernet0/7/0/18
unassigned GigabitEthernet0/7/0/19
unassigned GigabitEthernet0/7/0/20
unassigned GigabitEthernet0/7/0/21
unassigned GigabitEthernet0/7/0/22
unassigned GigabitEthernet0/7/0/23
unassigned GigabitEthernet0/7/0/24
unassigned GigabitEthernet0/7/0/25
unassigned GigabitEthernet0/7/0/26
unassigned GigabitEthernet0/7/0/27
unassigned GigabitEthernet0/7/0/28
unassigned GigabitEthernet0/7/0/29
unassigned GigabitEthernet0/7/0/30
unassigned GigabitEthernet0/7/0/31
unassigned GigabitEthernet0/7/0/32
unassigned GigabitEthernet0/7/0/33
unassigned GigabitEthernet0/7/0/36
unassigned GigabitEthernet0/7/0/37
unassigned GigabitEthernet0/7/0/38
unassigned GigabitEthernet0/7/0/39

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
51.51.51.51 Loopback0
1.20.30.40 MgmtEth0/RSP0/CPU0/0
unassigned MgmtEth0/RSP1/CPU0/0
unassigned GigabitEthernet0/3/0/1
unassigned GigabitEthernet0/3/0/3
unassigned TenGigE0/3/1/0
unassigned TenGigE0/3/1/3
unassigned TenGigE0/4/0/0
111.1.1.1 TenGigE0/5/1/1

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
protocol
'Down'
len('255.255.255.255')
15
'GigabitEthernet 0/7/0/15       unassigned       Up'.split()
['GigabitEthernet', '0/7/0/15', 'unassigned', 'Up']

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet 0/7/0/15

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
name
'GigabitEthernet0/7/0/39      un'
ipaddr
'assigned       Do'
status
'wn              Do'
protocol
'wn'
heading = 'Interface                    IP-Address       Status            Protocol'
heading.index('IP-Address')
29


data = ['texas', 'feb temp', 20, 25, 22, 17, 15, 8, 5, 10]
from statistics import mean
mean(data)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/statistics.py", line 258, in _exact_ratio
    return (x.numerator, x.denominator)
AttributeError: 'str' object has no attribute 'numerator'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#520>", line 1, in <module>
    mean(data)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/statistics.py", line 329, in mean
    T, total, count = _sum(data)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/statistics.py", line 188, in _sum
    for n, d in map(_exact_ratio, values):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/statistics.py", line 261, in _exact_ratio
    raise TypeError(msg)
TypeError: can't convert type 'str' to numerator/denominator
data = ['texas', 'feb temp', 20, 25, 22, 17, 15, 8, 5, 10]
it = iter(data)
state = next(it)
date = next(it)
state
'texas'
date
'feb temp'
mean(it)
15.25

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
heading
'Interface                    IP-Address       Status            Protocol\n'

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet 0/7/0/15
# Separate parts unlikely to change from parts likely to change

# Change:  data source        different filename        list of strings
# Change:  filtering on status up    and which fields to print

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
('GigabitEthernet0/7/0/39', 'unassigned', 'Down', 'Down')

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
[('Loopback0', '51.51.51.51', 'Up', 'Up'),
 ('MgmtEth0/RSP0/CPU0/0', '1.20.30.40', 'Up', 'Up'),
 ('MgmtEth0/RSP0/CPU0/1', 'unassigned', 'Down', 'Down'),
 ('MgmtEth0/RSP1/CPU0/0', 'unassigned', 'Up', 'Up'),
 ('HundredGigE0/1/0/0', 'unassigned', 'Shutdown', 'Down'),
 ('HundredGigE0/1/0/1', 'unassigned', 'Shutdown', 'Down'),
 ('TenGigE0/2/0/0', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/2/0/1', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/2/0/2', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/2/0/4', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/2/0/5', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/2/0/6', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/2/0/7', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/1', 'unassigned', 'Up', 'Up'),
 ('GigabitEthernet0/3/0/2', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/3', 'unassigned', 'Up', 'Up'),
 ('GigabitEthernet0/3/0/4', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/5', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/6', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/7', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/8', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/9', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/10', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/11', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/12', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/13', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/14', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/15', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/16', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/17', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/18', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/3/0/19', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/3/1/0', 'unassigned', 'Up', 'Up'),
 ('TenGigE0/3/1/1', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/3/1/2', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/3/1/3', 'unassigned', 'Up', 'Up'),
 ('GigabitEthernet0/4/0/0', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/4/0/0', 'unassigned', 'Up', 'Up'),
 ('GigabitEthernet0/4/0/1', 'unassigned', 'Down', 'Down'),
 ('TenGigE0/4/0/1', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/2', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/3', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/4', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/5', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/6', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/7', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/8', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/9', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/10', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/11', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/12', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/13', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/14', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/15', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/16', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/17', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/18', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/4/0/19', 'unassigned', 'Down', 'Down'),
 ('FortyGigE0/5/0/0', 'unassigned', 'Shutdown', 'Down'),
 ('FortyGigE0/5/0/1', 'unassigned', 'Shutdown', 'Down'),
 ('TenGigE0/5/1/0', 'unassigned', 'Shutdown', 'Down'),
 ('TenGigE0/5/1/1', '111.1.1.1', 'Up', 'Up'),
 ('GigabitEthernet0/7/0/0', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/1', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/2', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/3', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/4', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/5', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/6', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/7', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/8', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/9', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/10', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/11', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/12', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/13', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/14', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet 0/7/0/15', 'unassigned', 'Up', ''),
 ('GigabitEthernet0/7/0/16', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/17', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/18', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/19', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/20', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/21', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/22', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/23', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/24', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/25', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/26', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/27', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/28', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/29', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/30', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/31', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/32', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/33', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/36', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/37', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/38', 'unassigned', 'Down', 'Down'),
 ('GigabitEthernet0/7/0/39', 'unassigned', 'Down', 'Down')]

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
[Interface(name='Loopback0', ipaddr='51.51.51.51', status='Up', protocol='Up'),
 Interface(name='MgmtEth0/RSP0/CPU0/0', ipaddr='1.20.30.40', status='Up', protocol='Up'),
 Interface(name='MgmtEth0/RSP0/CPU0/1', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='MgmtEth0/RSP1/CPU0/0', ipaddr='unassigned', status='Up', protocol='Up'),
 Interface(name='HundredGigE0/1/0/0', ipaddr='unassigned', status='Shutdown', protocol='Down'),
 Interface(name='HundredGigE0/1/0/1', ipaddr='unassigned', status='Shutdown', protocol='Down'),
 Interface(name='TenGigE0/2/0/0', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/2/0/1', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/2/0/2', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/2/0/4', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/2/0/5', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/2/0/6', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/2/0/7', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/1', ipaddr='unassigned', status='Up', protocol='Up'),
 Interface(name='GigabitEthernet0/3/0/2', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/3', ipaddr='unassigned', status='Up', protocol='Up'),
 Interface(name='GigabitEthernet0/3/0/4', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/5', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/6', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/7', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/8', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/9', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/10', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/11', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/12', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/13', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/14', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/15', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/16', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/17', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/18', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/3/0/19', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/3/1/0', ipaddr='unassigned', status='Up', protocol='Up'),
 Interface(name='TenGigE0/3/1/1', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/3/1/2', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/3/1/3', ipaddr='unassigned', status='Up', protocol='Up'),
 Interface(name='GigabitEthernet0/4/0/0', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/4/0/0', ipaddr='unassigned', status='Up', protocol='Up'),
 Interface(name='GigabitEthernet0/4/0/1', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='TenGigE0/4/0/1', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/2', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/3', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/4', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/5', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/6', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/7', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/8', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/9', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/10', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/11', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/12', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/13', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/14', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/15', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/16', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/17', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/18', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/4/0/19', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='FortyGigE0/5/0/0', ipaddr='unassigned', status='Shutdown', protocol='Down'),
 Interface(name='FortyGigE0/5/0/1', ipaddr='unassigned', status='Shutdown', protocol='Down'),
 Interface(name='TenGigE0/5/1/0', ipaddr='unassigned', status='Shutdown', protocol='Down'),
 Interface(name='TenGigE0/5/1/1', ipaddr='111.1.1.1', status='Up', protocol='Up'),
 Interface(name='GigabitEthernet0/7/0/0', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/1', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/2', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/3', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/4', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/5', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/6', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/7', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/8', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/9', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/10', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/11', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/12', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/13', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/14', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet 0/7/0/15', ipaddr='unassigned', status='Up', protocol=''),
 Interface(name='GigabitEthernet0/7/0/16', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/17', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/18', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/19', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/20', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/21', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/22', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/23', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/24', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/25', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/26', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/27', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/28', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/29', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/30', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/31', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/32', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/33', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/36', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/37', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/38', ipaddr='unassigned', status='Down', protocol='Down'),
 Interface(name='GigabitEthernet0/7/0/39', ipaddr='unassigned', status='Down', protocol='Down')]


r = (0, 7)
r
(0, 7)
# This data could come from anywhere.
# If if you know the source, the data is not self-describing
print('happy' if r[0] == 0 else 'sad')
happy
from typing import NamedTuple
class TestResults(NamedTuple):
    failed: int
    attempted: int

    
r = TestResults(0, 7)

isinstance(r, tuple)
True
isinstance(r, TestResults)
True
len(r)
2
r[0]
0
r[1]
7
r
TestResults(failed=0, attempted=7)
r.failed
0
r.attempted
7
print('happy' if r[.failed == 0 else 'sad')
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
print('happy' if r.failed == 0 else 'sad')
      
happy

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet 0/7/0/15

================================= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py =================================
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet 0/7/0/15

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_ipv4.py
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet 0/7/0/15

# If you're parsing columns or writing regexes, you're
      
# living second milleneum.
      

# Go get better data:  JSON, YAML, XML, CSV
      
# Better because parsers are already written.
      



# TheHardWay
      
# TheEasyWay
      
movie = {'
         
SyntaxError: unterminated string literal (detected at line 1)
movie = {
    'raymond': 'Hunt for the Red October',
    'rachel': 'Gladiator',
    'matthew': 'Tron',
}
         
type(movie)
         
<class 'dict'>
len(movie)
         
3
'rachel' in movie
         
True
movie['matthew']
         
'Tron'
movie['numtwo']
         
Traceback (most recent call last):
  File "<pyshell#578>", line 1, in <module>
    movie['numtwo']
KeyError: 'numtwo'

movie.get('matthew', 'its a wonderful life')
         
'Tron'
movie.get('numtwo', 'its a wonderful life')
         
'its a wonderful life'
movie = {
    'raymond': 'Hunt for the Red October',
    'rachel': 'Gladiator',
    'matthew': 'Tron',
}
         
#        ^------- keys
         
#                 ^--- values
         
#        ^--------^--- items  (pairs)
         
y = movie.get('numtwo')
         
y is None
         
True
y = movie.get('numtwo', None)
         

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
{
    "bk103": {
        "description": "After the collapse of a nanotechnology \n      society in England, the young survivors lay the \n      foundation for a new society.", 
        "title": "Maeve Ascendant", 
        "price": 5.95, 
        "author": "Corets, Eva", 
        "publish_date": "2000-11-17", 
        "genre": "Fantasy"
    }, 
    "bk102": {
        "description": "A former architect battles corporate zombies, \n      an evil sorceress, and her own childhood to become queen \n      of the world.", 
        "title": "Midnight Rain", 
        "price": 5.95, 
        "author": "Ralls, Kim", 
        "publish_date": "2000-12-16", 
        "genre": "Fantasy"
    }, 
    "bk101": {
        "description": "An in-depth look at creating applications \n      with XML.", 
        "title": "XML Developer's Guide", 
        "price": 44.95, 
        "author": "Gambardella, Matthew", 
        "publish_date": "2000-10-01", 
        "genre": "Computer"
    }, 
    "bk107": {
        "description": "A deep sea diver finds true love twenty \n      thousand leagues beneath the sea.", 
        "title": "Splish Splash", 
        "price": 4.95, 
        "author": "Thurman, Paula", 
        "publish_date": "2000-11-02", 
        "genre": "Romance"
    }, 
    "bk106": {
        "description": "When Carla meets Paul at an ornithology \n      conference, tempers fly as feathers get ruffled.", 
        "title": "Lover Birds", 
        "price": 4.95, 
        "author": "Randall, Cynthia", 
        "publish_date": "2000-09-02", 
        "genre": "Romance"
    }, 
    "bk105": {
        "description": "The two daughters of Maeve, half-sisters, \n      battle one another for control of England. Sequel to \n      Oberon's Legacy.", 
        "title": "The Sundered Grail", 
        "price": 5.95, 
        "author": "Corets, Eva", 
        "publish_date": "2001-09-10", 
        "genre": "Fantasy"
    }, 
    "bk104": {
        "description": "In post-apocalypse England, the mysterious \n      agent known only as Oberon helps to create a new life \n      for the inhabitants of London. Sequel to Maeve \n      Ascendant.", 
        "title": "Oberon's Legacy", 
        "price": 5.95, 
        "author": "Corets, Eva", 
        "publish_date": "2001-03-10", 
        "genre": "Fantasy"
    }, 
    "bk109": {
        "description": "After an inadvertant trip through a Heisenberg\n      Uncertainty Device, James Salway discovers the problems \n      of being quantum.", 
        "title": "Paradox Lost", 
        "price": 6.95, 
        "author": "Kress, Peter", 
        "publish_date": "2000-11-02", 
        "genre": "Science Fiction"
    }, 
    "bk108": {
        "description": "An anthology of horror stories about roaches,\n      centipedes, scorpions  and other insects.", 
        "title": "Creepy Crawlies", 
        "price": 4.95, 
        "author": "Knorr, Stefan", 
        "publish_date": "2000-12-06", 
        "genre": "Horror"
    }, 
    "bk110": {
        "description": "Microsoft's .NET initiative is explored in \n      detail in this deep programmer's reference.", 
        "title": "Microsoft .NET: The Programming Bible", 
        "price": 36.00, 
        "author": "O'Brien, Tim", 
        "publish_date": "2000-12-09", 
        "genre": "Computer"
    }, 
    "bk111": {
        "description": "The Microsoft MSXML3 parser is covered in \n      detail, with attention to XML DOM interfaces, XSLT processing, \n      SAX and more.", 
        "title": "MSXML3: A Comprehensive Guide", 
        "price": 36.95, 
        "author": "O'Brien, Tim", 
        "publish_date": "2000-12-01", 
        "genre": "Computer"
    }, 
    "bk112": {
        "description": "Microsoft Visual Studio 7 is explored in depth,\n      looking at how Visual Basic, Visual C++, C#, and ASP+ are \n      integrated into a comprehensive development \n      environment.", 
        "title": "Visual Studio 7: A Comprehensive Guide", 
        "price": 49.95, 
        "author": "Galos, Mike", 
        "publish_date": "2001-04-16", 
        "genre": "Computer"
    }
}


= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
<class 'str'>

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
type(catalog)
         
<class 'dict'>

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
dict_keys(['bk103', 'bk102', 'bk101', 'bk107', 'bk106', 'bk105', 'bk104', 'bk109', 'bk108', 'bk110', 'bk111', 'bk112'])

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
dict_keys(['bk103', 'bk102', 'bk101', 'bk107', 'bk106', 'bk105', 'bk104', 'bk109', 'bk108', 'bk110', 'bk111', 'bk112'])

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk103
bk102
bk101
bk107
bk106
bk105
bk104
bk109
bk108
bk110
bk111
bk112
#  keys    values     items
         
#   ^-- default
         

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk103
bk102
bk101
bk107
bk106
bk105
bk104
bk109
bk108
bk110
bk111
bk112

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
{'description': 'After the collapse of a nanotechnology \n      society in England, the young survivors lay the \n      foundation for a new society.', 'title': 'Maeve Ascendant', 'price': 5.95, 'author': 'Corets, Eva', 'publish_date': '2000-11-17', 'genre': 'Fantasy'}
{'description': 'A former architect battles corporate zombies, \n      an evil sorceress, and her own childhood to become queen \n      of the world.', 'title': 'Midnight Rain', 'price': 5.95, 'author': 'Ralls, Kim', 'publish_date': '2000-12-16', 'genre': 'Fantasy'}
{'description': 'An in-depth look at creating applications \n      with XML.', 'title': "XML Developer's Guide", 'price': 44.95, 'author': 'Gambardella, Matthew', 'publish_date': '2000-10-01', 'genre': 'Computer'}
{'description': 'A deep sea diver finds true love twenty \n      thousand leagues beneath the sea.', 'title': 'Splish Splash', 'price': 4.95, 'author': 'Thurman, Paula', 'publish_date': '2000-11-02', 'genre': 'Romance'}
{'description': 'When Carla meets Paul at an ornithology \n      conference, tempers fly as feathers get ruffled.', 'title': 'Lover Birds', 'price': 4.95, 'author': 'Randall, Cynthia', 'publish_date': '2000-09-02', 'genre': 'Romance'}
{'description': "The two daughters of Maeve, half-sisters, \n      battle one another for control of England. Sequel to \n      Oberon's Legacy.", 'title': 'The Sundered Grail', 'price': 5.95, 'author': 'Corets, Eva', 'publish_date': '2001-09-10', 'genre': 'Fantasy'}
{'description': 'In post-apocalypse England, the mysterious \n      agent known only as Oberon helps to create a new life \n      for the inhabitants of London. Sequel to Maeve \n      Ascendant.', 'title': "Oberon's Legacy", 'price': 5.95, 'author': 'Corets, Eva', 'publish_date': '2001-03-10', 'genre': 'Fantasy'}
{'description': 'After an inadvertant trip through a Heisenberg\n      Uncertainty Device, James Salway discovers the problems \n      of being quantum.', 'title': 'Paradox Lost', 'price': 6.95, 'author': 'Kress, Peter', 'publish_date': '2000-11-02', 'genre': 'Science Fiction'}
{'description': 'An anthology of horror stories about roaches,\n      centipedes, scorpions  and other insects.', 'title': 'Creepy Crawlies', 'price': 4.95, 'author': 'Knorr, Stefan', 'publish_date': '2000-12-06', 'genre': 'Horror'}
{'description': "Microsoft's .NET initiative is explored in \n      detail in this deep programmer's reference.", 'title': 'Microsoft .NET: The Programming Bible', 'price': 36.0, 'author': "O'Brien, Tim", 'publish_date': '2000-12-09', 'genre': 'Computer'}
{'description': 'The Microsoft MSXML3 parser is covered in \n      detail, with attention to XML DOM interfaces, XSLT processing, \n      SAX and more.', 'title': 'MSXML3: A Comprehensive Guide', 'price': 36.95, 'author': "O'Brien, Tim", 'publish_date': '2000-12-01', 'genre': 'Computer'}
{'description': 'Microsoft Visual Studio 7 is explored in depth,\n      looking at how Visual Basic, Visual C++, C#, and ASP+ are \n      integrated into a comprehensive development \n      environment.', 'title': 'Visual Studio 7: A Comprehensive Guide', 'price': 49.95, 'author': 'Galos, Mike', 'publish_date': '2001-04-16', 'genre': 'Computer'}
ask 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk10
         
SyntaxError: invalid syntax


book
         
{'description': 'Microsoft Visual Studio 7 is explored in depth,\n      looking at how Visual Basic, Visual C++, C#, and ASP+ are \n      integrated into a comprehensive development \n      environment.', 'title': 'Visual Studio 7: A Comprehensive Guide', 'price': 49.95, 'author': 'Galos, Mike', 'publish_date': '2001-04-16', 'genre': 'Computer'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
{'description': "The two daughters of Maeve, half-sisters, \n      battle one another for control of England. Sequel to \n      Oberon's Legacy.", 'title': 'The Sundered Grail', 'price': 5.95, 'author': 'Corets, Eva', 'publish_date': '2001-09-10', 'genre': 'Fantasy'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva --> 2001-09-10

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva --> 2001-09-10

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

# \t    TAB    9
         
# \n    NL     10
         
# \N{name}   -> code point number
         

# \uNNNN     -> unicode code point
         

print('The answer is \u0664\u0662 today')
         
The answer is ٤٢ today
int('٤٢')
         
42
print('TheRaymondWay\u2122')
         
TheRaymondWay™
print('TheRaymondWay\N{trade mark sign}')
         
TheRaymondWay™

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
{'description': 'After the collapse of a nanotechnology \n      society in England, the young survivors lay the \n      foundation for a new society.', 'title': 'Maeve Ascendant', 'price': 5.95, 'author': 'Corets, Eva', 'publish_date': '2000-11-17', 'genre': 'Fantasy'}
{'description': 'A former architect battles corporate zombies, \n      an evil sorceress, and her own childhood to become queen \n      of the world.', 'title': 'Midnight Rain', 'price': 5.95, 'author': 'Ralls, Kim', 'publish_date': '2000-12-16', 'genre': 'Fantasy'}
{'description': 'An in-depth look at creating applications \n      with XML.', 'title': "XML Developer's Guide", 'price': 44.95, 'author': 'Gambardella, Matthew', 'publish_date': '2000-10-01', 'genre': 'Computer'}
{'description': 'A deep sea diver finds true love twenty \n      thousand leagues beneath the sea.', 'title': 'Splish Splash', 'price': 4.95, 'author': 'Thurman, Paula', 'publish_date': '2000-11-02', 'genre': 'Romance'}
{'description': 'When Carla meets Paul at an ornithology \n      conference, tempers fly as feathers get ruffled.', 'title': 'Lover Birds', 'price': 4.95, 'author': 'Randall, Cynthia', 'publish_date': '2000-09-02', 'genre': 'Romance'}
{'description': "The two daughters of Maeve, half-sisters, \n      battle one another for control of England. Sequel to \n      Oberon's Legacy.", 'title': 'The Sundered Grail', 'price': 5.95, 'author': 'Corets, Eva', 'publish_date': '2001-09-10', 'genre': 'Fantasy'}
{'description': 'In post-apocalypse England, the mysterious \n      agent known only as Oberon helps to create a new life \n      for the inhabitants of London. Sequel to Maeve \n      Ascendant.', 'title': "Oberon's Legacy", 'price': 5.95, 'author': 'Corets, Eva', 'publish_date': '2001-03-10', 'genre': 'Fantasy'}
{'description': 'After an inadvertant trip through a Heisenberg\n      Uncertainty Device, James Salway discovers the problems \n      of being quantum.', 'title': 'Paradox Lost', 'price': 6.95, 'author': 'Kress, Peter', 'publish_date': '2000-11-02', 'genre': 'Science Fiction'}
{'description': 'An anthology of horror stories about roaches,\n      centipedes, scorpions  and other insects.', 'title': 'Creepy Crawlies', 'price': 4.95, 'author': 'Knorr, Stefan', 'publish_date': '2000-12-06', 'genre': 'Horror'}
{'description': "Microsoft's .NET initiative is explored in \n      detail in this deep programmer's reference.", 'title': 'Microsoft .NET: The Programming Bible', 'price': 36.0, 'author': "O'Brien, Tim", 'publish_date': '2000-12-09', 'genre': 'Computer'}
{'description': 'The Microsoft MSXML3 parser is covered in \n      detail, with attention to XML DOM interfaces, XSLT processing, \n      SAX and more.', 'title': 'MSXML3: A Comprehensive Guide', 'price': 36.95, 'author': "O'Brien, Tim", 'publish_date': '2000-12-01', 'genre': 'Computer'}
{'description': 'Microsoft Visual Studio 7 is explored in depth,\n      looking at how Visual Basic, Visual C++, C#, and ASP+ are \n      integrated into a comprehensive development \n      environment.', 'title': 'Visual Studio 7: A Comprehensive Guide', 'price': 49.95, 'author': 'Galos, Mike', 'publish_date': '2001-04-16', 'genre': 'Computer'}
\N{trade mark sign}'
         
SyntaxError: unexpected character after line continuation character



book
         
{'description': 'Microsoft Visual Studio 7 is explored in depth,\n      looking at how Visual Basic, Visual C++, C#, and ASP+ are \n      integrated into a comprehensive development \n      environment.', 'title': 'Visual Studio 7: A Comprehensive Guide', 'price': 49.95, 'author': 'Galos, Mike', 'publish_date': '2001-04-16', 'genre': 'Computer'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
Fantasy
Fantasy
Computer
Romance
Romance
Fantasy
Fantasy
Science Fiction
Horror
Computer
Computer
Computer

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
{'description': 'An in-depth look at creating applications \n      with XML.', 'title': "XML Developer's Guide", 'price': 44.95, 'author': 'Gambardella, Matthew', 'publish_date': '2000-10-01', 'genre': 'Computer'}
{'description': "Microsoft's .NET initiative is explored in \n      detail in this deep programmer's reference.", 'title': 'Microsoft .NET: The Programming Bible', 'price': 36.0, 'author': "O'Brien, Tim", 'publish_date': '2000-12-09', 'genre': 'Computer'}
{'description': 'The Microsoft MSXML3 parser is covered in \n      detail, with attention to XML DOM interfaces, XSLT processing, \n      SAX and more.', 'title': 'MSXML3: A Comprehensive Guide', 'price': 36.95, 'author': "O'Brien, Tim", 'publish_date': '2000-12-01', 'genre': 'Computer'}
{'description': 'Microsoft Visual Studio 7 is explored in depth,\n      looking at how Visual Basic, Visual C++, C#, and ASP+ are \n      integrated into a comprehensive development \n      environment.', 'title': 'Visual Studio 7: A Comprehensive Guide', 'price': 49.95, 'author': 'Galos, Mike', 'publish_date': '2001-04-16', 'genre': 'Computer'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
Gambardella, Matthew → 2000-10-01
O'Brien, Tim → 2000-12-09
O'Brien, Tim → 2000-12-01
Galos, Mike → 2001-04-16

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
Gambardella, Matthew → 44.95
O'Brien, Tim → 36.0
O'Brien, Tim → 36.95
Galos, Mike → 49.95

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
Gambardella, Matthew → $44.95
O'Brien, Tim → $36.0
O'Brien, Tim → $36.95
Galos, Mike → $49.95

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
Gambardella, Matthew → $44.95
O'Brien, Tim → $36.00
O'Brien, Tim → $36.95
Galos, Mike → $49.95

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
Gambardella, Matthew → $44.95
O'Brien, Tim → $36.00
O'Brien, Tim → $36.95
Galos, Mike → $49.95

Task 7: Show tags and tag values for bk107
{'description': 'A deep sea diver finds true love twenty \n      thousand leagues beneath the sea.', 'title': 'Splish Splash', 'price': 4.95, 'author': 'Thurman, Paula', 'publish_date': '2000-11-02', 'genre': 'Romance'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
{book['author']} → $44.95
{book['author']} → $36.00
{book['author']} → $36.95
{book['author']} → $49.95

Task 7: Show tags and tag values for bk107
{'description': 'A deep sea diver finds true love twenty \n      thousand leagues beneath the sea.', 'title': 'Splish Splash', 'price': 4.95, 'author': 'Thurman, Paula', 'publish_date': '2000-11-02', 'genre': 'Romance'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
Gambardella, Matthew → $44.95
O'Brien, Tim → $36.00
O'Brien, Tim → $36.95
Galos, Mike → $49.95

Task 7: Show tags and tag values for bk107
{'description': 'A deep sea diver finds true love twenty \n      thousand leagues beneath the sea.', 'title': 'Splish Splash', 'price': 4.95, 'author': 'Thurman, Paula', 'publish_date': '2000-11-02', 'genre': 'Romance'}

= RESTART: /Users/raymond/Dropbox/Public/sj257/show_books.py
Task 1: Determine how many books are in the catalog
12

Task 2: Is bk152 in the catalog?
False

Task 3: Nicely display all the book identifiers
bk101
bk102
bk103
bk104
bk105
bk106
bk107
bk108
bk109
bk110
bk111
bk112

Task 4: Show all the book titles
Maeve Ascendant
Midnight Rain
XML Developer's Guide
Splish Splash
Lover Birds
The Sundered Grail
Oberon's Legacy
Paradox Lost
Creepy Crawlies
Microsoft .NET: The Programming Bible
MSXML3: A Comprehensive Guide
Visual Studio 7: A Comprehensive Guide

Task 5: Author, an arrow, publish date for bk105
Corets, Eva → 2001-09-10

Task 6: Author, an arrow and price for the computer books
Gambardella, Matthew → $44.95
O'Brien, Tim → $36.00
O'Brien, Tim → $36.95
Galos, Mike → $49.95

Task 7: Show tags and tag values for bk107
DESCRIPTION
A deep sea diver finds true love twenty 
      thousand leagues beneath the sea.

TITLE
Splish Splash

PRICE
4.95

AUTHOR
Thurman, Paula

PUBLISH_DATE
2000-11-02

GENRE
Romance


= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
# Test Driven Development.
         
# Write the tests AND then code.
         
# A problem well defined is half solved.
         
# Try out the API before you're written the code.
         
# Let's you specify clearly all expected behaviors.
         
# Runs and they fail.  Happy!  You haven't written the code
         
# yet.  Failure typically tests you what to do next.
         
# It is your coach.
         

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 4, in <module>
    from math_tools import square               # <-- Functions under test
ImportError: cannot import name 'square' from 'math_tools' (/Users/raymond/Dropbox/Public/sj257/math_tools.py)

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 4, in <module>
    from math_tools import square               # <-- Functions under test
ImportError: cannot import name 'square' from 'math_tools' (/Users/raymond/Dropbox/Public/sj257/math_tools.py)

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
F
======================================================================
FAIL: test_square (__main__.TestMathToolkit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 9, in test_square
    self.assertEqual(square(5), 25)     # <----- Test step 1
AssertionError: None != 25

----------------------------------------------------------------------
Ran 1 test in 0.008s

FAILED (failures=1)

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
F
======================================================================
FAIL: test_square (__main__.TestMathToolkit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 10, in test_square
    self.assertEqual(square(1), 1)      # <----- Test step 2
AssertionError: 25 != 1

----------------------------------------------------------------------
Ran 1 test in 0.008s

FAILED (failures=1)


3 + 3 + 3
         
9
4 + 4 + 4 + 4
         
16
5 + 5 + 5 + 5 + 5
         
25

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
E
======================================================================
ERROR: test_square (__main__.TestMathToolkit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 13, in test_square
    self.square('hello')
AttributeError: 'TestMathToolkit' object has no attribute 'square'

----------------------------------------------------------------------
Ran 1 test in 0.012s

FAILED (errors=1)

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
E
======================================================================
ERROR: test_square (__main__.TestMathToolkit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 13, in test_square
    self.square('hello')
AttributeError: 'TestMathToolkit' object has no attribute 'square'

----------------------------------------------------------------------
Ran 1 test in 0.008s

FAILED (errors=1)

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
.
----------------------------------------------------------------------
Ran 1 test in 0.006s

OK

= RESTART: /Users/raymond/Dropbox/Public/sj257/math_tools.py
square(5)
         
25
square(11)
         
121
square(0)
         
0

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 4, in <module>
    from math_tools import square, triple       # <-- Functions under test
ImportError: cannot import name 'triple' from 'math_tools' (/Users/raymond/Dropbox/Public/sj257/math_tools.py)

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
.F
======================================================================
FAIL: test_triple (__main__.TestMathToolkit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 16, in test_triple
    self.assertEqual(triple(5), 15)
AssertionError: None != 15

----------------------------------------------------------------------
Ran 2 tests in 0.021s

FAILED (failures=1)

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
.F
======================================================================
FAIL: test_triple (__main__.TestMathToolkit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 17, in test_triple
    self.assertEqual(triple(1), 3)
AssertionError: 15 != 3

----------------------------------------------------------------------
Ran 2 tests in 0.016s

FAILED (failures=1)
5 + 5 + 5
         
15
4 + 4 + 4
         
12

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.020s

OK
x = 10
         
x = x + 1
         
x += 1
         
x
         
12

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.018s

OK




= RESTART: /Users/raymond/Dropbox/Public/sj257/math_tools.py
square(-5)
         
0

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
.F.
======================================================================
FAIL: test_square_bug_117535 (__main__.TestMathToolkit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 24, in test_square_bug_117535
    self.assertEqual(square(-5), 25)
AssertionError: 0 != 25

----------------------------------------------------------------------
Ran 3 tests in 0.026s

FAILED (failures=1)
# 5 squared is 25    -5 squared is 25
         
# 4 squares is 16    -4 squared is 16
         

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.026s

OK

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.026s

OK
x = 10
         
-x
         
-10

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.026s

OK

= RESTART: /Users/raymond/Dropbox/Public/sj257/math_tools.py
square(25) / square(10)
         
6.25
square(25 / 10)
         
Traceback (most recent call last):
  File "<pyshell#643>", line 1, in <module>
    square(25 / 10)
  File "/Users/raymond/Dropbox/Public/sj257/math_tools.py", line 8, in square
    for i in range(x):
TypeError: 'float' object cannot be interpreted as an integer

square(2.5)
         
Traceback (most recent call last):
  File "<pyshell#645>", line 1, in <module>
    square(2.5)
  File "/Users/raymond/Dropbox/Public/sj257/math_tools.py", line 8, in square
    for i in range(x):
TypeError: 'float' object cannot be interpreted as an integer

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
..E.
======================================================================
ERROR: test_square_bug_117635 (__main__.TestMathToolkit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 28, in test_square_bug_117635
    self.assertEqual(square(2.5), 6.25)
  File "/Users/raymond/Dropbox/Public/sj257/math_tools.py", line 8, in square
    for i in range(x):
TypeError: 'float' object cannot be interpreted as an integer

----------------------------------------------------------------------
Ran 4 tests in 0.043s

FAILED (errors=1)
range(2.5)
         
Traceback (most recent call last):
  File "<pyshell#646>", line 1, in <module>
    range(2.5)
TypeError: 'float' object cannot be interpreted as an integer

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.033s

OK

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
...F
======================================================================
FAIL: test_triple (__main__.TestMathToolkit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj257/test_mathtools.py", line 19, in test_triple
    with self.assertRaises(TypeError):
AssertionError: TypeError not raised

----------------------------------------------------------------------
Ran 4 tests in 0.040s

FAILED (failures=1)

= RESTART: /Users/raymond/Dropbox/Public/sj257/math_tools.py
triple('hello')
         
'hellohellohello'

= RESTART: /Users/raymond/Dropbox/Public/sj257/math_tools.py

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.031s

OK
10 + 10 + 10
         
30


'hello' * 3
         
'hellohellohello'
'hello' + 3
         
Traceback (most recent call last):
  File "<pyshell#652>", line 1, in <module>
    'hello' + 3
TypeError: can only concatenate str (not "int") to str

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.035s

OK
'hello' * 3
         
'hellohellohello'
'hello' * 3 + 0
         
Traceback (most recent call last):
  File "<pyshell#654>", line 1, in <module>
    'hello' * 3 + 0
TypeError: can only concatenate str (not "int") to str
35.5 * 3
         
106.5
35.5 * 3 + 0
         
106.5

= RESTART: /Users/raymond/Dropbox/Public/sj257/test_mathtools.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.037s

OK


# BETA   FULL RELEASE  1.0
         
#                      1.1
         
#                      1.2
         

# 150 0.1     250 .5       325 0.4
         
# 150 0.1     250 Inf       325 -Inf
         

# 150 0.0     250 0.0       325 0.0
         


= RESTART: /Users/raymond/Dropbox/Public/sj257/github_restapi.py
{"login":"raymondh","id":167559,"node_id":"MDQ6VXNlcjE2NzU1OQ==","avatar_url":"https://avatars.githubusercontent.com/u/167559?v=4","gravatar_id":"","url":"https://api.github.com/users/raymondh","html_url":"https://github.com/raymondh","followers_url":"https://api.github.com/users/raymondh/followers","following_url":"https://api.github.com/users/raymondh/following{/other_user}","gists_url":"https://api.github.com/users/raymondh/gists{/gist_id}","starred_url":"https://api.github.com/users/raymondh/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/raymondh/subscriptions","organizations_url":"https://api.github.com/users/raymondh/orgs","repos_url":"https://api.github.com/users/raymondh/repos","events_url":"https://api.github.com/users/raymondh/events{/privacy}","received_events_url":"https://api.github.com/users/raymondh/received_events","type":"User","site_admin":false,"name":"Raymond Hettinger","company":"SauceLabs","blog":"","location":"Los Angeles and San Francisco California","email":null,"hireable":null,"bio":null,"twitter_username":null,"public_repos":0,"public_gists":0,"followers":129,"following":0,"created_at":"2009-12-14T20:09:05Z","updated_at":"2015-02-19T23:15:19Z"}
type(page)
         
<class 'str'>

= RESTART: /Users/raymond/Dropbox/Public/sj257/github_restapi.py
type(info){"login":"raymondh","id":167559,"node_id":"MDQ6VXNlcjE2NzU1OQ==","avatar_url":"https://avatars.githubusercontent.com/u/167559?v=4","gravatar_id":"","url":"https://api.github.com/users/raymondh","html_url":"https://github.com/raymondh","followers_url":"https://api.github.com/users/raymondh/followers","following_url":"https://api.github.com/users/raymondh/following{/other_user}","gists_url":"https://api.github.com/users/raymondh/gists{/gist_id}","starred_url":"https://api.github.com/users/raymondh/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/raymondh/subscriptions","organizations_url":"https://api.github.com/users/raymondh/orgs","repos_url":"https://api.github.com/users/raymondh/repos","events_url":"https://api.github.com/users/raymondh/events{/privacy}","received_events_url":"https://api.github.com/users/raymondh/received_events","type":"User","site_admin":false,"name":"Raymond Hettinger","company":"SauceLabs","blog":"","location":"Los Angeles and San Francisco California","email":null,"hireable":null,"bio":null,"twitter_username":null,"public_repos":0,"public_gists":0,"followers":129,"following":0,"created_at":"2009-12-14T20:09:05Z","updated_at":"2015-02-19T23:15:19Z"}