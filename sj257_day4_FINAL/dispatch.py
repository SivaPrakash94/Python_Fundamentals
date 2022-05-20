# Recommendation is that is a function has multiple signatures
# Just make two functions with different names.

from math import pi, sqrt

def square(x: int) -> int:
    return x ** 2

def smush_circle(r: float) -> float:
    area = pi * r ** 2
    side = sqrt(area)
    return side

## Could do, is put both in a single function #################

def box(x: int | float) -> int | float:
    if isinstance(x, int):
        return x ** 2
    if isinstance(x, float):
        return sqrt(pi * x ** 2)
    raise TypeError

## Single dispatch ############################################

# https://docs.python.org/3/library/functools.html#functools.singledispatch

from functools import singledispatch

@singledispatch
def sq(x):
    raise TypeError

@sq.register
def sq(x: int) -> int:
    return x ** 2

@sq.register
def sq(r: float) -> float:
    area = pi * r ** 2
    side = sqrt(area)
    return side
