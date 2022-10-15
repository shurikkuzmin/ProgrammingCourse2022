#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 09:42:35 2022

@author: shurik
"""

day = int(input("Please enter a number between 1 and 365: "))

if day < 1 or day > 365:
    print("Please enter a valid number")
    exit(0)

day_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

for i in range(12):
    print(months[i])

#if day <= 31:
#    print("January " + str(day))
#elif day <= 31 + 28:
#    print("February " + str(day - 31))
#elif day <= 31 + 28 + 31:
#    print("March " + str(day - 31 - 28))
#elif day <= 31 + 28 + 31 + 30:
#    print("April " + str(day - 31 - 28 - 31))
#elif day <= 31 + 28 + 31 + 30 + 31:
#    print("May " + str(day - 31 - 28 - 31 - 30))
#elif day <= 31 + 28 + 31 + 30 + 31 + 30:
#    print("June " + str(day - 31 - 28 - 31 - 30 - 31))
#elif day <= 31 + 28 + 31 + 30 + 31 + 30 + 31:
#    print("July " + str(day - 31 - 28 - 31 - 30 - 31 - 30))
#elif day <= 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31:
#    print("August " + str(day - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31))

