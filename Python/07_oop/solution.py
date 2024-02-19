# Car Class
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f'{self.__brand} {self.__model}'

    def get_brand(self):
        return self.__brand + '!'

    def set_brand(self, brand):
        self.__brand = brand

    def fuel_type(self):
        return 'Petrol or Diesel'

    @staticmethod
    def general_description():
        return 'Cars are amazing!'

    @property
    def model(self):
        return self.__model


# Electric Car Class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return 'Electric Charge'


my_car = Car('Toyota', 'RAV4')
my_electric_car = ElectricCar('Telsa', 'Model S', '80kWh')


# class Battery
class Battery:
    def battery_info(self):
        return 'This is battery'

# class Engine


class Engine:
    def engine_info(self):
        return 'This is engine'


# class ElectricCartwo
class ElectricCarTwo(Battery, Engine, Car):
    pass


my_new_car = ElectricCarTwo('Tesla', 'Model X2')

print(my_new_car.battery_info())
print(my_new_car.engine_info())
