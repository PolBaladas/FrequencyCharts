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
numbers = ['0','1','2','3','4','5','6','7','8','9']

def frequency(text, plot_bool):
    c = text
    letters_count = [0]*27
    i = 0
        
    while i<len(alpha):
        letters_count[i] = c.count(alpha[i])+c.count(alpha_cap[i])        
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
   

def numbers_frequency(text, plot_bool):
    c = text    
    numbers_count = [None]*10
    i = 0
        
    while i<len(numbers_count):
        numbers_count[i] = c.count(numbers[i])        
        i+=1

    
    if(plot_bool):
        fig = plt.figure()        
        width = .35
        ind = np.arange(len(numbers_count))
        plt.bar(ind, numbers_count)
        plt.xticks(ind + width/2, numbers)
        return(numbers_count)
    else:
        return(numbers_count)
