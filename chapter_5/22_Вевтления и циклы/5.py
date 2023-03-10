"""
Составить программу нахождения действительных и комплексных корней
квадратного уравнения ax^2 + bx + c = 0.
Исходные данные: a, b, c
Результат: действительные корни: x1 и x2, -
или комплексные корни: x1 + ix2 и x1 - ix2

___________________
Тестовые значения:
a   b   c       x1      x2
2   4   10      -1+2i   -1-2i
4   10  5       -0.69   -1.81
"""
from math import sqrt, fabs

a = 4
b = 10
c = 5

D = b**2 - 4*a*c
if D >= 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(round(x1, 2), round(x2, 2))
else:
    x1 = -b/(2*a)
    x2 = sqrt(fabs(D))/(2*a)
    print(complex(x1, x2), complex(x1, -x2))





