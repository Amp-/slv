"""
Дана строка, содержащая русскоязычный текст.
Найти количество слов, начинающихся с буквы “е”.

-------------------
Тестовый пример:

Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели. (7 слов)
"""

s = "Ежевику для ежат " \
    "Принесли два ежа." \
    "Ежевику еле-еле" \
    "Ежата возле ели съели."

count_E = s.count('Е')
count_e = s.count(' е')
count_res = count_E + count_e
print('Count: ', count_res)



