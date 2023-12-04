# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:33:13 2023

@author: student
"""


def lista_razem(lista_1, lista_2):
    lista_razem = lista_1 + lista_2
    lista_razem = list(set(lista_razem))
    wynik_listy = [i ** 3 for i in lista_razem]
    return wynik_listy


lista_1 = [10, 9, 7, 4, 5]
lista_2 = [1, 2, 3, 4, 5]

wynik = lista_razem(lista_1, lista_2)
print(wynik)
