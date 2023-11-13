# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:04:17 2023

@author: student
"""


def wyswietl_parzyste(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)
           
liczby = list(range(11))
wyswietl_parzyste(liczby)
