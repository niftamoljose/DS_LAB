#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:21:12 2022

@author: sjcet
"""
#1)
#2)
import matplotlib.pyplot as plt
import numpy as np
x=np.array(["mon","tues","wed","thurs","fri","sat"])
y=np.array([130,120,135,130,150,80])
plt.plot(x,y,color='blue', linestyle="dotted")
plt.xlabel("days")
plt.ylabel("no. of absentees")
plt.show()