class Car():
    car_count = 0

    def __init__(self):
        self.name = 'corolla'
        self._model = 'toyota'
        self.__year = 1999

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self.__year

    def set_year(self,year):
        self.__year = year

c= Car()
print(c.get_year())
c.set_year(2022)
print(c.get_year())