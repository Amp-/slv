import random

ls = list(range(100,1001,5))

lst = random.sample(ls,50)
print(sum(lst))