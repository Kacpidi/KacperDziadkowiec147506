# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:12:37 2023

@author: student
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        srednia_ocen = sum(self.marks) / len(self.marks)
        return srednia_ocen > 50


student1 = Student("Kacper Dziadkowiec", [60, 70, 80, 90])
student2 = Student("Julia Steczko", [40, 30, 20, 10])

print(f"{student1.name} zaliczył: {student1.is_passed()}")
print(f"{student2.name} zaliczyła: {student2.is_passed()}")
