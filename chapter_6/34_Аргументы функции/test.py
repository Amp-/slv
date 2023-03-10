def func(**kwargs):
    print(kwargs)

func(a=1,b=2,c=3)


def shop(kind,*args,**kwargs):
    print(kind)
    print("*" * 50)

    for t in args:
        print(t)
    print("*" * 50)

    for t,k in kwargs.items():
        print(f'Ключ {t} значение {k}')

shop(123,1,2,3,a=1,b=2,c=3)


