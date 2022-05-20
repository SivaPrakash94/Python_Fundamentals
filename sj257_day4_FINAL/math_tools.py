'This will be the product we are making: a math library'

def square(x):
    'Return a value times itself'
    return x * x

def triple(x):
    'Return value added to itself thrice'
    # We add zero here to trigger a mandatory TypeError non-numbers
    # This is *much* faster than an isinstance() check.
    return x * 3 + 0
