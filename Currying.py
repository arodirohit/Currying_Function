# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:02:54 2019

@author: Rohit.A.R
"""

def change(a): 
    def w(b): 
        def x(c): 
            print(a+b+c) 
        return x 
    return w 
   
change(10)(20)(30)