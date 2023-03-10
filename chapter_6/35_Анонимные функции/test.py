def test(n):
    return lambda x: x+n


f=test(10)
print(f(1))
pairs = [(1, 'one'), (2, 'two'), (4, 'four'), (3, 'tree')]
pairs.sort(key=lambda pair: pair[0])
print(pairs)