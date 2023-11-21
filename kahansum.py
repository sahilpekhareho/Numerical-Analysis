# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:36:06 2023

@author: delegates
"""
import math

#kahan sum

def kahansum(xs):
    s = 0.; e = 0.
    for x in xs:
        temp = s
        y = x + e
        s = temp + y
        e = (temp - s) + y
    return s

xt = 1.e20
yt = -1.e20
zt = 1

listnum = [xt,yt,zt]
print(kahansum(listnum))



    
    