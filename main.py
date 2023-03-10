import sys
import pandas
csv1 = "../../Downloads/#lng=37.46046;lat=55.81540;zoom=17.csv"
csv = "../../Downloads/#lng=37.46140;lat=55.81412;zoom=16.csv"
street = 'улица Габричевского'
street1 = 'Волоколамское шоссе'

house = '8'


# with open("./1.txt","w") as f:
#     f.writelines(data.keys()+'\n')
def show_comments(csv,street,house):
    data = pandas.read_csv(csv, low_memory=False)
    data_street = data[data['yandex_address_street'] == street]
    data_home = data_street[data_street['yandex_address_house'] == house]
    data_list = data_home['yandex_address_doorcode'].to_list()
    print(f'Всего {len(data_list)}')
    test = set(data_list)
    print(f'Всего {len(test)}')
    for t in test:
        if(len(str(t))>3):
            print(t)

def show_pass_yandex(csv,street,house,entrance):
    ent = str(entrance)
    data = pandas.read_csv(csv, low_memory=False)
    data_street = data[data['yandex_address_street'] == street]
    data_home = data_street[data_street['yandex_address_house'] == house]
    data_ent = data_home[data_home['yandex_address_entrance'] == ent]
    data_list = data_ent['yandex_address_doorcode'].to_list()
    print(f'Всего {len(data_list)}')
    data_set = set(data_list)
    #print(f'Всего {len(data_set)}')
    count=0
    for t in data_set:
         if(len(str(t))>3):
            count += 1
            print(t)
    print(f'Найдено {count} кода(ов) подходящих под заданные условия')

def show_user_data(csv,surname):
    data = pandas.read_csv(csv, low_memory=False)
    data_user = data[data['yandex_name'] == surname]
    data_list = data_user['yandex_address_doorcode'].to_list()
    data_set = set(data_list)
    for t in data_set:
        if (len(str(t)) > 3):
            print(t)


#show_pass_yandex(csv,street,house,1)
# show_user_data(csv,"Андрей")
print(sys.builtin_module_names)


