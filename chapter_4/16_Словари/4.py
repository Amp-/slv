"""
Дан словарь {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}.
Найти 3 наибольших значения в нем.
"""

d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

values = d.values()
sor_val = sorted(values,reverse=True)
print(sum(sor_val[0:3]))