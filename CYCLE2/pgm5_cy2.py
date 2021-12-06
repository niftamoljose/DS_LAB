#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:23:46 2021

@author: sjcet
"""
import numpy as np
array=np.array([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28])
print("Elements from index 2 to 8 with step 2",array[2:8:2])
print("Last 3 elements of the array using negative index",array[-3:-1])
print("Alternate elements of the array",array[::2])
print("Display the last 3 alternate elements",array[-3:-1:2])
