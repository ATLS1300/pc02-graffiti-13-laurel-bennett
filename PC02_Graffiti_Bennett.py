#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Laurel Bennett
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

color("green")
width(5)
up()
forward(150)
down()
circle(50,180)
circle(-50,180)
up()
left(90)
forward(40)
left(105)
forward(60)
left(100)
down()
forward(245)
right(90)
up()
forward(500)
right(180)
down()
circle(50,180)
circle(-50,180)
up()
left(90)
forward(60)
left(105)
forward(60)
left(100)
down()
forward(260)
up()
left(90)
forward(350)
left(90)
forward(10)
right(90)
color("purple")
width(3)
down()
circle(25)
up()
forward(30)
right(100)
forward(5)
right(5)
down()
circle(25)
right(100)
forward(20)
right(70)
up()
forward(115)
right(10)
down()
color("brown")
forward(100)
backward(120)
forward(120)
right(45)
forward(50)
right(45)
forward(50)
right(45)
forward(50)
right(45)
forward(160)
left(90)
width(4)
forward(50)
right(180)
forward(220)
backward(50)
right(90)
width(3)
forward(50)











