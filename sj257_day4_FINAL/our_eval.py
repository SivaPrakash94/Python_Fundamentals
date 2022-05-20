'Homegrown, reduced functionality version of eval'

# Goal:  Teach lots of core Python
#     len  split  int  [1 : -1]  if-elif-else
#     try/except  k in d   d[k]    None
#     print   [0]     a,b,c=t   def f()
#     while  continue

# Side goals:
#     Get a feel for what eval() does.
#     Get a feel for what shell repl() does.

# * Gain an appreciation for how dicts simplify code.
# * Drill in the notion of dunder methods:
#           '+'   -->  '__add__'
# * Show the __name__ / __main__ test

import sys

ns = {'x': 10, 't': 'hello', 's': [10, 20, 30],
      'template': 'the answer is %s today'}

operator_map = {
    '+':    '__add__',
    '-':    '__sub__',
    '*':    '__mul__',
    '/':    '__truediv__',
    '//':   '__floordiv__',
    '%':    '__mod__',
    '**':   '__pow__',
    '$$':   '__mydunder__',  # I can extend the lang with new operators
}

def myeval(s, ns=ns):
    tokens = s.split()
    if len(tokens) == 1:
        p = tokens[0]
        if p.isdigit():                 # integers have digits
            return int(p)
        if p[0] == p[-1] == '"':        # strings can have double quotes
            return p[1 : -1]
        if p[0] == p[-1] == "'":        # strings can have single quotes
            return p[1 : -1]
        if p.isidentifier():            # variables are known identifiers
            if p not in ns:
                raise NameError(f'Unknown variable {p!r}')
            return ns[p]
    if len(tokens) == 3:
        p, op, q = tokens
        if op in operator_map:
            method_name = operator_map[op]
            pv = myeval(p, ns)
            qv = myeval(q, ns)
            return getattr(pv, method_name)(qv)
    raise SyntaxError(f'Unknown token: {tokens!r}')

def repl():
    'Read-eval-print-loop'
    print('FakePython Shell')
    print('----------------\n')
    prompt = '>>> '
    while True:
        expr = input(prompt)
        try:
            value = myeval(expr)
        except Exception as e:
            print('Doh!', file=sys.stderr)
            print(e, file=sys.stderr)
            continue
        if value is not None:
            print(repr(value))
        ns['_'] = value

if __name__ == '__main__':

    repl()
