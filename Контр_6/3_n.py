import texttable
from Students_n import Students

students_AI_file = 'AI_students.txt'
students_IS_file = 'IS_students.txt'


students_Ai = Students(students_AI_file, "Applied Informatics")
students_IS = Students(students_IS_file,"Information Security")


all_students = students_Ai.get_students_list(sort=True)
all_students.extend(students_IS.get_students_list(sort=True))

table = texttable.Texttable()
table.set_cols_align(['l', 'l', 'l', 'c', 'c', 'c', 'c'])
table.set_cols_width([20, 15, 25, 6, 10, 10, 10])
table.set_precision(1)

headers=['Name', 'Birthday', 'Speciality', 'Year', 'Group', 'Entry points', 'Avg points']
data = [headers]
data.extend(all_students)
table.add_rows(data)
print(table.draw())