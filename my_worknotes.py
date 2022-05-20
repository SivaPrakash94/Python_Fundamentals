states = ['texas', 'iowa', 'ohio', 'iowa', 'utah']
print(len(states))
print(states[0])
print([state.title() for state in states])
states.append('hawaii')
print(states)
states = ['texas', 'iowa', 'ohio', 'iowa', 'utah']
print(len(states))
print(states[0])
print([state.title() for state in states])
states.append('hawaii')
print(states)
print(states.pop())         # LIFO stack:  Removes and returns rightmost element (undoes an append)
states.insert(0, 'alaska')  # Don't do this.  It moves ALL the data to the right and does not scale welxl.
print(states)
print(states.sort())        # Typically None is returned to indicate mutated data
print(states)
print(states.reverse())
print(states)

try:
    print(states[6])
except IndexError:
    print("Oops, I did it again. I indexed too far. I'm not that innocent.")