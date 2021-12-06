#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:17:47 2021

@author: sjcet
"""

import numpy as np
x=np.array([[2,3,5,4],[1,5,6,3],[8,5,6,2],[9,7,6,4]])
print(x)
print ("display all elements excluding first row")
print(x[1:])
print("display all elements excluding last column")
print(x[:,:3])
print("display elemets of second and third row ")
print(x[1:3])
print("Display the elements of first and second column in second and third row")
print("Display second and third element of first row")
print(x[0,1])
print(x[0,2])