class Resistor:

    def __init__(self, resistance):
        self.x = resistance
    def __repr__(self):
        return f'Resistor({self.x})'
    def __str__(self):
        return f'{self.x:.1f}\N{ohm sign}'
    def current(self, *, voltage): # * to tell the right side args needs to be NAMED while the function call
        "Computed the current given the voltage using Ohm's law"
        return voltage / self.x
    def series(self, *other_resistors):
        if not all([isinstance(other, Resistor) for other in other_resistors]):
            raise TypeError('Expected all resistors')
        return Resistor(self.x + sum([other.x for other in other_resistors]))

    def parallel(self, *other_resistors):
        if not all([isinstance(other, Resistor) for other in other_resistors]):
            raise TypeError('Expected all resistors')
        return Resistor(1/ ((1/self.x) +
                            sum([1/ other.x for other in sother_resistors])))

        # return Resistor((1/ self.x) + (1 /other.x))

    def __add__(self, other):
        return self.series(other)
    def __mul__(self, other):
        return self.parallel(other)
    def __eq__(self, other):
        return type(self) == type(other) and self.x == other.x

        
        
        
        

r1 = Resistor(100)
print(vars(r1))
print(repr(r1))
print(r1)
print(r1.current(voltage=50))

r2 = Resistor(200)

print(r1.series(r2))
print(r1.series(r2, r1))

r1 = Resistor(6)
r2 = Resistor(8)
r3 = Resistor(4)
r4 = Resistor(8)
r4 = Resistor(4)
r6 = Resistor(6)
r7 = Resistor(8)
r8 = Resistor(10)
r9 = Resistor(6)
r10 = Resistor(2)

r_eq = ((((r8 + r10) * r9 + r7) * r6 + r5) * r4 + r3) * r2 + r1
print(r_eq.current(voltage=12), 'amps')
