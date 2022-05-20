'Develop a class as shown in Test.pdf'

class Resistor:
    "Model the behavior of a resistor in a circuit"

    def __init__(self, resistance):
        self.x = resistance

    def __repr__(self):
        return f'Resistor({self.x})'

    def __str__(self):
        return f'{self.x:.1f}\N{ohm sign}'

    def current(self, *, voltage):
        "Compute the amperage given the voltage using Ohm's law."
        # Ohm's law:  V = IR
        return voltage / self.x

    def series(self, *other_resistors):
        "Resistor equivalent for one or more resistors in parallel"
        if not all([isinstance(other, Resistor) for other in other_resistors]):
            raise TypeError('Expected all resistors')
        return Resistor(self.x + sum([other.x for other in other_resistors]))

    def parallel(self, *other_resistors):
        "Resistor equivalent across two resistors wired in parallel"
        if not all([isinstance(other, Resistor) for other in other_resistors]):
            raise TypeError('Expected all resistors')
        return Resistor(1 / ((1 / self.x) +
                             sum([1 / other.x for other in other_resistors])))

    def __add__(self, other):
        return self.series(other)

    def __mul__(self, other):
        return self.parallel(other)

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.x == other.x


if __name__ == '__main__':

    r1 = Resistor(100)
    print(vars(r1))
    print(repr(r1))
    print(r1)
    print(r1.current(voltage=50))
    r2 = Resistor(200)
    print(r1.series(r2))
    print(r1.parallel(r2))
    print(r1 + r2)
    print(r1 * r2)
    print(r1 == Resistor(100))

    print((Resistor(8).series(Resistor(4))).parallel(Resistor(12)).series(Resistor(6)))
    print((Resistor(8) + Resistor(4)) * Resistor(12) + Resistor(6) == Resistor(12))

    r1 = Resistor(6)
    r2 = Resistor(8)
    r3 = Resistor(4)
    r4 = Resistor(8)
    r5 = Resistor(4)
    r6 = Resistor(6)
    r7 = Resistor(8)
    r8 = Resistor(10)
    r9 = Resistor(6)
    r10 = Resistor(2)

    r_eq = ((((r8 + r10) * r9 + r7) * r6 + r5) * r4 + r3) * r2 + r1
    print(r_eq.current(voltage=12), 'amps')
