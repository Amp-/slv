from Students_n import Students
import random,texttable


students_AI_file = 'AI_students_upd.txt'
students_IS_file = 'IS_students_upd.txt'


students_Ai = Students(students_AI_file, "Applied Informatics")
students_IS = Students(students_IS_file,"Information Security")


all_students = students_Ai.get_students_list(year=5,short_info=True)
all_students.extend(students_IS.get_students_list(year=5,short_info=True))


random.shuffle(all_students)

max_st_per_day = 5
cur_day = 1
st_by_days = {}

for i in range(0,len(all_students),max_st_per_day):
    st_by_days[cur_day] = all_students[i:i+max_st_per_day]
    cur_day +=1

table = texttable.Texttable()
table.set_cols_align(['l', 'l', 'l', 'c', 'c'])
table.set_cols_width([20, 15, 25, 6, 10])
table.set_precision(1)

headers = ['Name', 'Birthday', 'Speciality', 'Group', 'Avg points']

for day, st_list in st_by_days.items():
    print(f'\nThe {day} day:\n')
    data = [headers]
    data.extend(st_list)
    st_list = sorted(st_list,key= lambda s: s[0])
    table.add_rows(data)
    print(table.draw())
    table.reset()