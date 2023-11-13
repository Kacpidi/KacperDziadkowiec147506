# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:59:00 2023

@author: student
"""
#Zadanie 2b
def pomnoz_przez_2_for(lista):
    for i in range(len(lista)):
        lista[i] *= 2
    return lista
liczby = [5, 6, 7, 8, 9]
wynik = pomnoz_przez_2_for(liczby)
print(wynik)


def pomnoz_przez_2_list_comprehension(lista):
    return [x * 2 for x in lista]
liczby = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_2_list_comprehension(liczby)
print(wynik)