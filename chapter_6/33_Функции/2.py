"""
Дана последовательность целых чисел.
Найти минимальное среди простых чисел и максимальное среди чисел, не являющихся простыми.
"""
l = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]

def is_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

def is_neutral(n):
    return n in [0, 1]

min_l = max(l)  #100000000
max_l = min(l)  #-1000000000

for i in l:
    if is_neutral(i):
        continue

    is_pr = is_prime(i)
    if is_pr and i<min_l:
        min_l = i
    elif not is_pr and i>max_l:
        max_l = i

print('Min: ', min_l)
print('Max: ', max_l)
