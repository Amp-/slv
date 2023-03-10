class Car():
    car_count = 0
    def __init__(self):
        self.name = 'corolla'
        self._model = 'toyota'
        self.__year = 1999

    def public_method(self):
        print("Public method")

    def _protected_method(self):
        print("Protected method")

    def __private_method(self):
        print("Private method")

c = Car()

print(c.name)
print(c._model)
print(c._Car__year)
#print(c.__year) вернет ошибку