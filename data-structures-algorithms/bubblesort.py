# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#This file will demonstrate the Bubble Sort algorithm

def bubbleSort(theList):
    for i in range (0, len(theList) - 1):
        for j in range(0, len(theList) - 1 - i):
            if theList[j] > theList[j+1]:
                theList[j], theList[j+1]= theList[j+1], theList[j]
    return theList

myList = ['c','a','h','g','s','b']
print(bubbleSort(myList))

##followed link
##https://www.youtube.com/watch?time_continue=151&v=YHm_4bVOe1s&feature=emb_title