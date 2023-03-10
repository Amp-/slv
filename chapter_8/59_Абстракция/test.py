from abc import ABC, abstractmethod

class People(ABC):
    def __init__(self,name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        print(f"{self.name},{self.surname},{self.age}")

    @abstractmethod
    def main_info(self):
        pass

class Emplyee(People):
    def __init__(self,name,surname,age,position):
        super().__init__(name,surname,age)
        self.position = position

    def get_info(self):
        print(f"{self.name},{self.surname},{self.age},{self.position}")

    def main_info(self):
        print(f"{self.name}, {self.surname}")

emp1 = Emplyee("Andrey","Petrov",34,"Eng")

emp1.get_info()
emp1.main_info()