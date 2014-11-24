# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:23:28 2014

@author: polbaladas
"""


import numpy as np
import matplotlib.pyplot as plt

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
'r','s','t','u','v','w','x','y','z']

number = ['1','2','3','4','5','6','7','8','9','0']

def frequency(text, plot_bool):
    c = text
    letters = []
    letters_count = [0]*27
    numbers = []    
    numbers_count = [None]*27
    i = 0
        
    while i<len(alpha):
        letters_count[i] = c.count(alpha[i])        
        i+=1

    i = 0
    while i<len(number):
        numbers_count[i] = c.count(number[i])        
        i+=1
    
    
    if(plot_bool):
        fig = plt.figure()        
        width = .35
        ind = np.arange(len(letters_count))
        plt.bar(ind, letters_count)
        plt.xticks(ind + width/2, alpha)
        return(letters_count)
    else:
        return(letters_count)
   

