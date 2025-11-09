from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, licence_plate, year):
        self.__licence_plate = licence_plate
        self.__year = year

    def get_license(self):
        if self.__licence_plate:
            return self.__licence_plate

        return None

    def get_year(self):
        if self.__year:
            return self.__year

        return None

    def set_license_plate(self, licence):
        if licence:
            self.__licence_plate = licence

    def set_year(self, year):
        if year:
            self.__year = year

    @abstractmethod
    def calculate_annual_tax(self):
        pass
