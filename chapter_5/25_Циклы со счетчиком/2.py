"""
Дано натуральное число N. Определить количество делителей этого числа K, не равных ему самому.
Например, для N = 12 такие делители: 1, 2, 3, 4, 6, а их количество K = 5.

-------------------
Тестовые данные:
12 (1, 2, 3, 4, 6) = 5
20 (1,2,4,5,10) = 5
35 (1,5, 7) = 3
"""
N = 35
K = 0

for i in range(1, N//2+1):
    if N%i == 0:
        K += 1

print(K)
