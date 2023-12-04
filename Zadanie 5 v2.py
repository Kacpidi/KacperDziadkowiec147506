# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:21:09 2023

@author: student
"""


def sprawdz_wartosc_w_liscie(lista, wartosc):
    if wartosc in lista:

        return True
    else:

        return False


lista_1 = [7, 8, 9, 10, 11, 12]
wartosc = 15
wynik = sprawdz_wartosc_w_liscie(lista_1, wartosc)


print(wynik)
