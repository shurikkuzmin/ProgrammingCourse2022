#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 09:53:01 2022

@author: shurik
"""

num = int(input("Please enter a number: "))

num2 = num
for i in range(2, int(num / 2) + 1):
    counter = 0
    while num2 % i == 0:
        num2 = int(num2 / i)
        counter = counter + 1
    if counter > 0:
        print("Number " + str(num) + " is divided by " 
              + str(i) + "^" + str(counter))