#print(dir())
#import os
#os.getcwd()
#print(os.listdir('./data'))

# Deallocation happens immediately.
# when no reference, it gets deallocated

#NAMESPACES                                 HEAP
# globals: o----------------------------------^
# heap cares about if the object exists or not

#import this

#d =Dict()
# makes an instant

s = 'the tale of two cities'

#s.upper()

#ask  
# python objects are immutable except for dict, list 
# get item, set item
# what is a repr? repr() ' ' --> interactive shell will display the repper except for None
# 

#print(dir(str))

#print (help(str.join))
#t=s.split()
#print("<->" .join(t))


# _ is a previous variable

#30 + 40
#_ + _ 
#(140)

# .__contains__ -- > in
#.rstrip(), lstrip, (strip removes all \n \t etc characters)
#The major difference between str() and repr() is intended audience. repr() is intended to produce output that is mostly machine-readable (in many cases, it could be valid Python code even), whereas str() is intended to be human-readable.


#range(start, stop, step)
#range(10,20,2) --> 10, 12, 14, 16, 18

#lambda is a quick function that gets deleted after use in 1 line

print((lambda x: x ** 3)(5))

s = 'the tale of two cities'
case = 'upper'
getattr(s, case) ()
case = 'title'
getattr(s, case) ()
#print(dir(s))

#pv.__mul__(5) --> getattr(pv, method_name)(qv)
#all methods kind of call its own instance name
#function dont. That's the only difference
#methods automatically put instance name in the 1st argument
#f' is called a f string
#polymorphism is not what a class does but what programmers do.
# same function name in 2 classes

#All test code showed should be in if __name__ = 'main' :
#so you can have your test sample run but when you import, that test code wont be executed

# Dunder methods CAN be called directly.
#__str__ gets called when you say print()
#print(obj) --> sys.stdout.write(obj.__str__)
#Class(a,b) --> Class.__init__(self, a, b)
# use .casefold() for case insensitive comparison: if status.casefold() == 'up'
# f'{ipaddr:15} {name}' --> give 15 space gap in btw ipaddr and name

# ''' This is a docstring ''' --> .__doc__
def add_binary(a, b):
    '''
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum


#print(add_binary.__doc__)

#by default while accessing dicts, keys are used
# for book_id in sorted(catalog) --> catalog is dict and keys are taken for book_id
#\N{name} is a unicode code point. /n is next line
#\N{rightwards arrow} is -> 
#print('THeRaymondWay\u2122') is as same as:
#print('THeRaymondWay\N{trade mark sign}')
#f string has formarter as well--> :.2f says format: 2 points after decimal
# f"{book['price]}:.2f"
import json
from pprint import pprint 
from urllib.request import urlopen
url = 'https://api.github.com/users/raymondh'
with urlopen(url) as f:
    #page = f.read().decode()
    #print(page)
    info = json.load(f)

pprint(info)

#DAY4
# FUNCTION CALLS
# * --> order matters .tuple
# ** --> name matters . Dicts

# __str__ is a subset of __repr__
# __str__ = __rpr__.()
# change only rpr to get both str and rpr changed
# change str and rpr to have different values 
# raw string is r'' --> no need to add special chars for special chars
# r'\bme\b' --> '\\bme\\b' (without r)
