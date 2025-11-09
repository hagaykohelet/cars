from classes.car import Car
from classes.electric_mixin import ElectricMixin
from classes.luxury_mixin import LuxuryMixin
from classes.engine import Engine

class ElectricCar(Car, ElectricMixin, LuxuryMixin):
    def __init__(self, licence_plate, year, engine: Engine):
        super().__init__(licence_plate, year,engine)
        self.engine = engine

    def calculate_annual_tax(self):
        tax = 250
        return tax


