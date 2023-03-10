dict1 = {'name': 'Alex', 'age': 12, 'class': 'v', 'roll_id': '2'}
check = ['class', 'Alex', 'Michael', '4', 2, '2', 'age', 'address', ('name', 'Alex'), ('class', 'x')]
for t in check:
    if (t in dict1):
        print('True')
    else:
        print('False')
