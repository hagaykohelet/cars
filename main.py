from classes.car import Car
from classes.electric_car import ElectricCar
from classes.electric_mixin import ElectricMixin
from classes.engine import Engine
from classes.luxury_mixin import LuxuryMixin
from classes.truck import Truck
from classes.vehicle import Vehicle

if __name__ == "__main__":
    engine_car = Engine("benzin", 200)
    car = Car("12-345-67", 2020, engine_car)

    engine_electric_cer = Engine("electric", 150)
    electric_car = ElectricCar("123-45-678", 2021, engine_electric_cer)

    truck = Truck("98-765-43", 2023, 400)
    cars_list = [car, electric_car, truck]
    for vehicle in cars_list:
        print(vehicle.calculate_annual_tax())

    print(truck.get_license())
    truck.set_license_plate("45-678-21")
    print(truck.get_license())

    print(electric_car.get_luxury_mixin())
    electric_car.charge()
