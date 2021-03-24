# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:06:55 2020

@author: Wayland Singh
"""

#test rig for multiplying numbers together in O(n) time
import numpy as np

nums = np.array([1,2,3,4]*10)

def mult(nums):
    narray = np.array([nums for _ in nums])
    for i in range(len(nums)):
        narray[i,i] =1
    result = narray.prod(axis=1)
    return result
    
mult(nums)