# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:24:24 2019

@author: y.reyes
"""

def removeElement(nums: list, val: int) -> int:
    """ Funcion que devuelve la longintud de una lista luego de removerle el valor especificado """
    
    
    while val in nums:
        nums.remove(val)
    
    return len( nums )

