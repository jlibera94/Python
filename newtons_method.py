# -*- coding: utf-8 -*-
"""
Created on Sun May 13 00:40:33 2018

@author: John
"""

def f(x):
    return 9 - x*(x-10)

def fprime(x):
    return -2*x + 10

#selecting initial guess
intl_guess = -10

for val in range(1,10):
    nextGuess = intl_guess -f(intl_guess)/fprime(intl_guess)
    print(nextGuess)
    intl_guess = nextGuess
