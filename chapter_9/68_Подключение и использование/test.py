import random

a = random.randrange(0, 10)  # возвращает случацное число
print(a)

b = random.randint(0, 10)
print(b)

lst = list(range(0,10))
c = random.choice(lst)
print(c)

random.shuffle(lst)
print(lst)

print(random.sample(lst,4))

print(random.random())

