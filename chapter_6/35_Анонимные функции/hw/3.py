l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count1 = 0
count2 = 0
res = list(map(lambda x:x%2==0,l))
for t in res:
    if t==True:
        count1 +=1
    else:
        count2 +=1
print(count1)
print(count2)