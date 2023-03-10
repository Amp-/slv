l = [
    {'name': 'And', 'age': '33', 'place': 'Moscow'},
    {'name': 'Serg', 'age': '38', 'place': 'Srp'},
    {'name': 'Konst', 'age': '34', 'place': 'Yaroslavlv'}
]

res = sorted(l, key=lambda x: x.keys() == 'age')
l.sort(key=lambda x:x['age'])
print(l)