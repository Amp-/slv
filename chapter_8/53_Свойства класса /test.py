#static
class Car():
    car_count = 0
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
    def start(self):
        Car.car_count +=1


c = Car("bmw","x1","2012")
c.start()
print(c.car_count)
c1 = Car("bmw","x2","2012")
c1.start()
print(c1.car_count)

#dynamic
class Car():
    car_count = 0
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        self.car_count +=1

c = Car("bmw","x1","2012")
print(c.car_count)
c1 = Car("bmw","x2","2012")
print(c1.car_count)
print(Car.car_count)