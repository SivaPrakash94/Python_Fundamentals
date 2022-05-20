'Our homegrown interactive shell that mimics a shell called IPython'

In = [None]
Out = [None]

print('Welcome to BetterShell\N{trade mark sign}')
print('=======================')
while True:
    prompt = f'\nIn [{len(In)}]: '
    expr = input(prompt)
    if expr == 'quit':
        break
    value = eval(expr)
    if value is not None:
        print(f'Out[{len(Out)}]: {value!r}')
    In.append(expr)
    Out.append(value)

