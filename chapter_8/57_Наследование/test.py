class People():
    def __init__(self,name,surname,year):
        self.name = name
        self.surname = surname
        self.year = year

    def get_info(self):
        print(f'{self.name}, {self.surname}, {self.year}')

class Employee(People):
    def __init__(self, name,surname,year,position):
        super().__init__(name,surname,year)
        self.position = position

    def get_info(self):
        print(f'{self.name}, {self.surname}, {self.year}, {self.position}')

emp = Employee("Andr","Gush","33","Test")

emp.get_info()