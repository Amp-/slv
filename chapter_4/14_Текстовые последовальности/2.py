"""
Дана строка, заканчивающаяся точкой.
Подсчитать, сколько слов в строке.
"""

s = "Ежевику для ежат ; Принесли два ежа."
s= s.replace(',','')
s= s.replace(';','')
s= s.replace(':','')
s= s.replace('.','')

count_word = s.split()

print(len(count_word))