#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:40:46 2022

@author: shurik
"""
def factorial_for_loop(crocodile):
    fact = 1
    for i in range(1, crocodile + 1):
        fact = fact * i
    return fact

def factorial_recursion(parrot):
    fact = 1
    if parrot == 1:
        return fact
    else:
       fact = parrot * factorial_recursion(parrot - 1)
    return fact
num = int(input("Please enter a number: "))

print(factorial_for_loop(num))
print(factorial_recursion(num))