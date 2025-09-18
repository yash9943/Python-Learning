# Class
# Objects
# Inheritance
# Encapsulations
# Polymorphism
# Class Variables
# Static Methods
# isinstance()

class Car:
    total_car = 0  # Class Variable
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def genral_description():
        return "This is a car"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric"
        
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_tesla = ElectricCar("Tesla", "Model S", "100 kWh")
# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.full_name())
# print(my_tesla.fuel_type())

# safariThree = Car("Tata", "Nexon")
# car = Car("Hyundai", "Creta")
# print(safari.fuel_type())

# test = Car("test","test")
# print(Car.total_car)

# safari = Car("Tata", "Safari")
# print(safari.genral_description())
# print(Car.genral_description())
# print(safari.model)

# my_tesla = ElectricCar("Tesla", "Model S", "100 kWh")
# print(isinstance(my_tesla, ElectricCar))
# print(isinstance(my_tesla, Car))


''' Mulitiple Inheritance '''

class Battery:
    def battery_info(self):
        return "This is a battery"

class Engine:
    def engine_info(self):
        return "This is an engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model 3")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())