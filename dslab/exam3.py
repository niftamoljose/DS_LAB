#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:24:00 2022

@author: sjcet
"""
#1
#3)
import matplotlib.pyplot as plt
import numpy as np
x=np.array(["mon","tues","wed","thurs","fri","sat"])
y=np.array([130,120,135,130,150,80])
plt.plot(x,y)
plt.plot(x,y,'D' ,mfc ="yellow")
plt.title("attendence record of class VIII")
plt.xlabel("days")
plt.ylabel("no. of absentees")
plt.show()