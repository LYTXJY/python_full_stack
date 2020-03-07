# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:26:42 2020

@author: xjy
"""


import turtle as t

t.pensize(4)
# t.hideturtle()
t.colormode(255)
t.color((255, 155, 192), "pink")
t.setup(840, 500)
t.speed(10)

#t.write("我在哪",font=("华文琥珀",20,"normal"))

#鼻子
t.pu()#原来pu()==penup(),缩写为pu
t.goto(-100,100)
t.pd()#同理，pd()==pendown(),缩写为pd()
t.seth(-30)
t.begin_fill()
a = 0.4
for i in range(120):
    if i <= i < 30 or 60 <= i <90:
        a += 0.08
        t.lt(3)#向左转3°
        t.fd(a)#向前走a的步长
    else:
        a = a - 0.08
        t.lt(3)
        t.fd(a)
        t.end_fill()

#
#
#
#
#


t.done()