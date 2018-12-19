# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:42:36 2018

@author: John
"""

import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    #create turtle - draw square
    turt = turtle.Turtle()
    turt.color('yellow')
    turt.shape('turtle')
    turt.speed(3)
    
    for i in range (1,36):
        draw_square(turt)
        turt.right(9)
        
        
    window.exitonclick()
    
draw_art()