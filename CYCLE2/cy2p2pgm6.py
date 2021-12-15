#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:38:54 2021

@author: sjcet
"""

import numpy as np
A = np.array ([[2,-2,3],
              [7,8,1],
              [4,-9,5]])
B = np.array([[2],
             [4],
             [8]])
inv = np.linalg.inv(A)
x = np.linalg.solve(inv ,B)
print(x)