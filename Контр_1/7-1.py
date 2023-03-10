s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s_union = s1.union(s2)
s_inter= s1.intersection(s2)
s_sym_dif = s1.symmetric_difference(s2)
print(s_union)
print(s_inter)
print(s_sym_dif)

com_elem = s1 & s2
s1 -= com_elem
print('s1 uniq elem', s1)
tmp_s = {4, 5, 6}
print(f's2 is superset for {tmp_s} : {s2 >= tmp_s}' )
tmp_s = {8, 4, 3}
print(f's2 is superset for {tmp_s} : {s2 >= tmp_s}' )
tmp_s = {5, 8, 4, 7, 6}
print(f's2 is superset for {tmp_s} : {s2 > tmp_s}' )