class Car():
    def __init__(self,name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def start(self):
        print("start")

    def stop(self):
        print("stop")


bmw = Car("x1","bmw",2008)
print(bmw.name)