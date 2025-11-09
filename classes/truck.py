from classes.vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, licence_plate, year, max_load):
        super().__init__(licence_plate, year)
        self.max_load = max_load

    def calculate_annual_tax(self):
