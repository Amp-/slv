"""""
c=(F-32)*5/9
F = C * 9/5 +32


"""

t='610f'
T = int(t[0:-1])
suffix = t[-1]
print(suffix)

if suffix=='C' or suffix =='c':
    F = (T * 9 / 4) + 32
    print(f'{T} Цельсия это {round(F)} Фаренгейту')
elif suffix=='F' or suffix == 'f':
    C = (T - 32) * 5/9
    print(f'{T} по Фаренгейту это {C} Цельсия')
else:
    print("Ошибка")
