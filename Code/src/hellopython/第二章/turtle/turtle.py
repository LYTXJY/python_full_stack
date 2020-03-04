# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 08:57:24 2020

@author: xjy
"""


import turtle as tl

tl.color("blue")
tl.circle(100)
# tl.done()#必须加上这句话，保持turtle绘图程序继续运行，否则会无响应，卡死。

tl.penup()
tl.goto(-200, 0)
tl.pendown()
tl.color("yellow")
tl.circle(100)

tl.penup()
tl.goto(200, 0)
tl.pendown()
tl.color("green")
tl.circle(100)

tl.penup()
tl.goto(-100, 0)
tl.pendown()
tl.right(180)
tl.color("red")
tl.circle(100)

tl.penup()
tl.goto(100, 0)
tl.pendown()
# tl.right(180)
tl.color("black")
tl.circle(100)

tl.done()