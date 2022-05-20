'Oue Homegrown interactive shell'

#prompt = ': '
In = [None]
Out = [None]

print('Welcome to BetterShell\N{trade mark sign}')

while True:
    prompt = f'\nIn[{len(In)}]: '
    expr = input(prompt)
    value = eval(expr)
    if expr == 'quit':
        break
    if value is not None:
        print(f'\nOut[{len(Out)}: {value!r}')
        In.append(expr)
        Out.append(value)
        

