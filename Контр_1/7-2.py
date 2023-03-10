math = {'Matvei', 'Evgeniya', 'Michail', 'Maxim', 'Natalia'}
physics = {'Maxim', 'Matvei', 'Alexandr'}

all_win = math.union(physics)
print(all_win)

both = math & physics
print(both)

math=both
del physics
print()