# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:28:11 2023

@author: student
"""


# Zadanie 3

def sprawdzaj_parzysta(number):
    return number % 2 == 0


wynik = sprawdzaj_parzysta(9)
if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
