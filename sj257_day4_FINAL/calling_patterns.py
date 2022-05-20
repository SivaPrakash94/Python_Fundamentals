'Goal:  Learn how to pack and unpack data in function calls'

def mypow(base, exp):
    'Computes base to the power to the exponent'
    return base ** exp

print(mypow(2, 5))                          # Positional arguments -- Order matters
print(mypow(exp=5, base=2))                 # Keyword arguments -- Name matters
print(mypow(2, exp=5))                      # Hybrid form has a rule -- Positional arguments go before Keyword arguments

arguments = (2, 5)                          # Cheap luggage: tuple.  Small and fast and ordered.
print(mypow(arguments[0], arguments[1]))    # TSA makes you unpack your bags before traveling with a function call
print(mypow(*arguments))                    # ONE star in a function CALL will UNPACK any SEQUENCE into POSITIONAL args where ORDER matters

arguments = {'exp': 5, 'base': 2}           # Expensive luggage: dict.  Larger and slower but allows lookup by name.
print(mypow(exp=arguments['exp'], base=arguments['base']))    # TSA makes you unpack your bags before traveling with a function call
print(mypow(**arguments))                   # TWO stars in a functional CALL will UNPACK any MAPPING into KEYWORD args where the NAME matters

def f(a, b, c=0, d=0):                      # These are called DEFAULT arguments or OPTIONAL arguments
    return a + b + c + d

print(f(10, 20))
print(f(10, 20, 5))
print(f(10, 20, 5, 7))
print()

def f(a, b, *t, **d):
    print(a)
    print(b)
    print(t)                                 # ONE star in a function DEFINITION will PACK excess POSITIONAL arguments into a TUPLE where ORDER matters
    print(d)                                 # TWO stars in a function DEFINITION will PACK excess KEYWORD arguments into a DICT where NAME matters  

f(10, 20, 5, 7, 12, x=111, y=222, z=333)

def logging_pow(*args, **kwargs):            # Wrapper functions delegate core logic to another function and just add some "extras"
    "Print out calls to mypow()"
    answer = mypow(*args, **kwargs)
    print(f'mypow() called with {args} and {kwargs} giving {answer}')
    return answer

y = logging_pow(2, 5)
y = logging_pow(exp=5, base=2)
y = logging_pow(2, exp=5)

def g(a, b, c, d, e, f):                     # Uses are free to mix and match positional and keyword arguments  
    print(a, b, c, d, e, f)

g(10, 20, 30, 40, 50, 60)
g(10, 20, 30, f=60, e=50, d=40)
g(f=60, e=50, d=40, c=30, b=20, a=10)

def g(a, b, /, c, d, *, e, f):               # The slash restrict args to the left to POSITIONAL-ONLY. The star applies right to KEYWORD-ONLY
    print(a, b, c, d, e, f)

g(10, 20, 30, f=60, e=50, d=40)              # This is allowed
# g(10, 20, 30, 40, 50, 60)                  # This is rejected because the STAR requires e and f to be keyword args
# g(f=60, e=50, d=40, c=30, b=20, a=10)      # This is rejected because the SLASH requires a and b to be positional arg

# Put restrictions in early.  You can take them off later if needed.
# It is hard to add restrictions later without breaking code.

# Advantages of positional-only:
# * later you can change the argument name                          len(obj)  -> len(sizeable)
# * slightly faster than keyword calls
# * makes parameter name available for use in keyword

# Advantages of keyword-only:
# * Force improved readability                                      sorted('cat', reverse=True)
# * Allows reordering                                               *, action, message ->  *, message, action
# * Works better for deprecation                                    f(*, a, b, c, d=0) -> f(*, a, b, d=0)
