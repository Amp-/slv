l = [1,20,3,55,7,8,38,4,25,33]

max_elem = max(l)
max_elem_index = l.index(max_elem)
print(f'Максимальный элемент {max_elem} индекс {max_elem_index}')

del l[max_elem_index+1:]

print(l)