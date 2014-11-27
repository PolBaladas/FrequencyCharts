# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:23:28 2014

@author: polbaladas
"""


import numpy as np
import matplotlib.pyplot as plt
import string

alpha = string.ascii_lowercase
alpha_cap = string.ascii_uppercase

def frequency(text, plot_bool):
    c = text
    letters_count = [0]*27
    #numbers_count = [None]*27
    i = 0
        
    while i<len(alpha):
        letters_count[i] = c.count(alpha[i])+c.count(alpha_cap[i])        
        i+=1

    #i = 0
    #while i<len(number):
    #    numbers_count[i] = c.count(number[i])        
    #    i+=1
    
    
    if(plot_bool):
        fig = plt.figure()        
        width = .35
        ind = np.arange(len(letters_count))
        plt.bar(ind, letters_count)
        plt.xticks(ind + width/2, alpha)
        return(letters_count)
    else:
        return(letters_count)
   

