#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:55:51 2021

@author: sjcet
"""

import matplotlib.pyplot as plt
import numpy as np
  

x = [1,2,3,4,5]
y = [3,3,3,3,3]
z = [2,4,6,8,10]

plt.plot(x, y, label = "line 1")
plt.plot(y, z, label = "line 2")
plt.plot(x,z, label = "line 3")
plt.legend()
plt.show()