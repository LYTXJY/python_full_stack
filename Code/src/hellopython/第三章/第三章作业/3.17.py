# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:23:59 2020

@author: xjy
"""

#3.17

#已知三点，求三角形面积（或求三个内角）

x1, y1 = eval(input("请输入第一个点： "))
x2, y2 = eval(input("请输入第一个点： "))
x3, y3 = eval(input("请输入第一个点： "))

import turtle as t
t.hideturtle()
t.pu()
t.colormode(255)
t.color(231, 26, 95)


t.goto(x1, y1)
t.pd()
t.begin_fill()

t.goto(x2, y2)
t.write(x2,y2, font = ("华文琥珀", 10))
t.goto(x3, y3)
t.write(x3, y3)
t.goto(x1, y1)
t.write(x1, y1, font = ("仿宋", 10))
t.end_fill()

area = 0.5 * (x1*y2 + x2*y3 + x3 * y1 -y1*x2 - y2 * x3 - y3 * x1 )
t.write("三角形面积是：%f " % area)
t.done()

