#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:00:41 2022

@author: shurik
"""

import random

success = 0
for case in range(100000):
    arr = []
    for i in range(23):
        arr.append(random.randint(1,365))
    if len(set(arr)) < 23:
        success = success + 1

print("Probability is " + str(success / 100000))