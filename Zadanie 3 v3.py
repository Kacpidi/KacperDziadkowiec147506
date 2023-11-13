# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:02:18 2023

@author: student
"""

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.area} sqm, {self.rooms} rooms, priced at {self.price}, located at {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {self.area} sqm, {self.rooms} rooms, priced at {self.price}, located at {self.address}, plot size {self.plot} sqm"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.area} sqm, {self.rooms} rooms, priced at {self.price}, located at {self.address}, on floor {self.floor}"

house = House(500, 10, "500,000 USD", "Sikorek 3", 2000)

flat = Flat(100, 3, "300,000 USD", "Słowikow 5", 2)

print(house)
print(flat)
