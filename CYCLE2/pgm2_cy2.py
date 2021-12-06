#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 12:08:39 2021

@author: sjcet
"""

import numpy as np
arr=np.array([[2,3,5],[6,2,8]],dtype='c')
newarr=arr.reshape(3,2)
print(newarr)
