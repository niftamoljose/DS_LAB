#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:27:06 2021

@author: sjcet
"""
import numpy as np
from numpy import array
from scipy.linalg import svd
from numpy import dot
from numpy import diag
A = array([[1,3,1], [3,5,2], [5,8,4]])
print(A)
print(" SVD")
U, s, VT = svd(A)
print(U)
print(s)
print(VT)
Sigma=diag(s)
B=U.dot(Sigma.dot(VT))
print(B)

