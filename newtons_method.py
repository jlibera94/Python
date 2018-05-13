# -*- coding: utf-8 -*-
"""
Created on Sun May 13 00:40:33 2018

@author: John
"""

def f(x):
    return 9 - x*(x-10)

def fprime(x):
    return -2*x + 10

guess = -10

for val in range(1,10):
    nextGuess = guess -f(guess)/fprime(guess)
    print(nextGuess)
    guess = nextGuess