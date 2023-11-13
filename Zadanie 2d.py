# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:16:39 2023

@author: student
"""


def wyswietl_co_drugi(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])
        
liczby = list(range(11))
wyswietl_co_drugi(liczby)
