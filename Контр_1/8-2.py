import math

goods = {'smart watch': 550, 'phone': 1000, 'playstation': 500, 'laptop': 1550, 'music player': 600, 'tablet': 400}

print(sum(goods.values()))

list_goods = goods.keys()
print(sorted(list_goods))


goods['music'] = round(600 / 2)
print(goods)

price_laptop_table = goods['laptop']*3 + goods['phone']*5
count_table = math.ceil(price_laptop_table / goods['tablet'])
print(count_table)

gift = goods.popitem()
print(gift)
print(goods)

goods.update({'iphone' : 1300, 'music player' : 850, 'headphones' : 200})
print(goods)


