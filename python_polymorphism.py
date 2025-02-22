#polymorphism  many form  to a class or object 
#len()  #str , list , tuple , dict , set

name_string = "swetha"
print(len(name_string))
name_list = ["surya", "teja", "swetha"]
print(len(name_list))

class Vechile:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("Vechile is moving")
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Car is moving")
class Bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Bike is moving")

car = Car("Toyota", "Camry")
vechile = Vechile("Bus")
bike = Bike("Suzuki", "Swift")
for _vehicle_ in (car, vechile, bike):
    _vehicle_.move()
