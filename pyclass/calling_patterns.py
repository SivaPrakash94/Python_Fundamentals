def mypow (base, exp):
    return base ** exp

def g(a, b, /, c, d, *,e,f):
    print(a,b,c,d,e,f)


names = 'manny jo jack'.split()

print([name.capitalize() for name in names])

print([name.capitalize() for name in names if name.startswith('m')])

print([len(name) for name in names])


print([f'{name}' for name in names])


