#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:00:41 2022

@author: shurik
"""

import random

num_people = 41
num_cases = 10000

success = 0
for case in range(num_cases):
    arr = []
    for i in range(num_people):
        arr.append(random.randint(1,365))
    if len(set(arr)) < num_people:
        success = success + 1

print("Probability is " + str(success / num_cases))