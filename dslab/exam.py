#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:59:46 2022

@author: sjcet
"""
#1

import matplotlib.pyplot as plt
import numpy as np
x=np.array(["mon","tues","wed","thurs","fri","sat"])
y=np.array([130,120,135,130,150,80])
plt.bar(x,y, width=0.1)
plt.title("attendence record of class VIII")
plt.xlabel("days")
plt.ylabel("no. of absentees")
plt.show()