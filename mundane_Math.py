# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:12:24 2019

@author: Wayne Monteiro
"""

sum=0

for i in range(1,100):
    if i%2==0:
        sum = sum +i
    else:
        sum=sum
    
print ("sum of the num=",sum)