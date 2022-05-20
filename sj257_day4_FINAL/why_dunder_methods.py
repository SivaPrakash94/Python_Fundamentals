'''

Easy ways (short-cuts)      Actual way (real method)          Adjective 
----------------------      ------------------------          ---------

a + b                       a.__add__(b)                      Addable
a - b                       a.__sub__(b)
a * b                       a.__mul__(b)
a / b                       a.__truediv__(b)
a // b                      a.__floordiv__(b)
a ** b                      a.__pow__(b)
a % b                       a.__mod__(b)
b in a                      a.__contains__(b)                 Container
a[b]                        a.__getitem__(b)                  Indexable
a(b, c)                     a.__call__(b, c)                  Callable
a.b                         a.__getattribute__('b')


repr(a)                     a.__repr__()
str(a)                      a.__str__() 
len(a)                      a.__len__()                       Sizeable   
vars(a)                     a.__dict__
type(a)                     a.__class__
divmod(a, b)                a.__divmod__(b)
pow(a, b)                   a.__pow__(b)
print(a, b)                 sa = a.__str__()
                            sys.stdout.write(sa)
                            sys.stdout.write(' ')
                            sb = b.__str__()
                            sys.stdout.write(sb)
                            sys.stdout.write('\n')                            


for b in a:                 it = a.__iter__()                 a: Iterable it: Iterator
   <body>                   while True:
                                try:
                                    b = it.__next__()         
                                except StopIteration:
                                    break
                                <body>

with a as b:                b = a.__enter__()                 Context Manager 
   <body>                   try:
                               <body>
                            except Exception as e:
                                a.__exit__(type(e), e, traceback(e)
                            else:
                                a.__exit__(None, None, None)
                               

'''



# Python is a fully object oriented language.
# Everything in Python is an object
# Object: str int dict list functions classes exceptions file
# Objects are encapsulated.
# The ONLY way to interact with an object is through its methods.
# Methods do EXACTLY what their class defines them to do.

# Do we HAVE TO use "with"?  or HAVE TO use "for"?  HAVE TO use "+"   HAVE TO use "print".
#       GET TO                  GET TO              GET TO            GET TO


# No, you don't HAVE TO do anything, you could just use methods.
# Yes, you GET TO use nices approachs that call methods for you.


# Raymond, do I HAVE TO do things the easy way?
# Answer:  No!

colors = ['red', 'green', 'blue']
for color in colors:
    print(len(color), color.upper())

# Here, go it do it the hard way:

import sys

it = colors.__iter__()
while True:
    try:
        color = it.__next__()
    except StopIteration:
        break
    size = color.__len__()
    size_str = size.__str__()
    cup = color.upper()
    cup_str = cup.__str__()
    sys.stdout.write(size_str)
    sys.stdout.write(' ')
    sys.stdout.write(cup_str)
    sys.stdout.write('\n')
    
        
