"""
Даны длины сторон треугольника.
Проверить, является ли треугольник равносторонним, равнобедренным или разносторонним.
"""
a = 20
b = 20
c = 20

if a == b == c:
    print("Треугольник равносторонний")
elif a == b or b == c or a == c:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторонний")
