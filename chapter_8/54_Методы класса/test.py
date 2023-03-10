class Car():
    car_count = 0
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
    @classmethod
    def inc_car_count(cls):
        cls.car_count += 1

    def start(self):
        Car.inc_car_count()

    @staticmethod
    def is_valid_model(model):
        models = ["Toyota","Honda","BMW","2"]
        return model in models


print(Car.car_count)
car= Car(1,"2",3)
car.start()
print(car.is_valid_model(car.model))
print(Car.car_count)
Car.inc_car_count()
print(Car.car_count)
print(car.car_count)
print(Car.is_valid_model("Honda"))

