dict1 =  {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'], 'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']}

dict1['pocket'] = ['seashell', 'strange berry', 'lint']
dict2 = {}
dict2['backpack'] = dict1['backpack']
print(sorted(dict2.items()))
print(dict2)
#код неверный иду дальше