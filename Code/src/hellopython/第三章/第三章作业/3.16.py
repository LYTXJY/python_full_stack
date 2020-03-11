# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:20:22 2020

@author: xjy
"""


#3.16
import turtle as t

t.screensize(1024, 763)
t.showturtle()
t.hideturtle()
t.colormode(255)

#三角形
t.begin_fill()
t.color(213, 56, 87)
for i in range(0, 3):
    t.fd(100)
    t.lt(120)
    
t.end_fill()

#t.reset()

#正方形
t.begin_fill()
t.color(89, 90, 255)
for i in range(0, 4):
    t.fd(100)
    t.lt(90)
t.end_fill()
#t.reset()

#五边形
t.begin_fill()
t.color(189, 190, 255)
for i in range(0, 5):
    t.fd(100)
    t.lt(72)
t.end_fill()
#t.reset()

#六边形
t.begin_fill()
t.color(19, 255, 2)
for i in range(0, 5):
    t.fd(100)
    t.lt(60)
t.end_fill()
#t.reset()


t.done()