l = [
    ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom'),
    ('test', 'sort', 'bort', 'cook', 'egg', 'dad'),
    ('tom', 'bom', 'dom', 'lom', 'kom', 'som'),
]

l.sort(key=lambda x:x[2][::-1])
print(l)
