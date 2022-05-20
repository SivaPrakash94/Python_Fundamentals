'Our homegrown interactive shell that Mimics that standard Python shell'

prompt = '>>> '
while True:
    expr = input(prompt)
    value = eval(expr)
    if value is not None:
        print(repr(value))
    _ = value
