s = 'Дана строка. Проверить, сколько слов заканчивается на букву “я” '
lst = s.split()
count = 0
for t in lst:
    if(t.endswith('я') == True):
        count +=1
print(count)
