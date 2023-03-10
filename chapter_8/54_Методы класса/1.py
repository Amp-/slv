"""
Изменить класс “Дробь” следующим образом:
- все статические свойства классов должны изменяться только внутри классовых методов;
- выделить один или несколько вспомогательных методов (если это не было сделано ранее)
и оформить их в виде статических методов.

"""
class Fraction():
    proper_fr_count = 0
    improper_fr_count = 0

    @classmethod
    def inc_fr_count(cls, is_proper):
        if is_proper:
            cls.proper_fr_count += 1
        else:
            cls.improper_fr_count += 1

    def set(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.inc_fr_count(numerator < denominator)

    def print(self):
        print('\u0332'.join(f'{self.numerator}  '))
        print(f'{self.denominator}')

    def get_reversed(self):
        print('The reversed fraction of')
        self.print()
        print('is: ')
        rev_fr = Fraction()
        rev_fr.set(self.denominator, self.numerator)
        rev_fr.print()

    @staticmethod
    def get_nod(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def reduce(self):
        nod = Fraction.get_nod(self.numerator, self.denominator)
        if nod != 1:
            print('The fraction')
            self.print()
            print('after reduction is: ')
            self.set(self.numerator//nod, self.denominator//nod)
            self.print()
        else:
            print('The fraction')
            self.print()
            print("can't be reduced!")


f1 = Fraction()
f1.set(5, 10)
f1.print()
f1.get_reversed()

f2 = Fraction()
f2.set(8, 3)
f2.print()

f3 = Fraction()
f3.set(5, 5)
f3.print()
f3.reduce()

f4 = Fraction()
f4.set(12, 36)
f4.print()
f4.reduce()

f5 = Fraction()
f5.set(3, 2)
f5.print()

print(f'Proper fractions count: {Fraction.proper_fr_count}')
print(f'Improper fractions count: {Fraction.improper_fr_count}')