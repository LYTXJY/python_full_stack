# -*- coding: utf-8 -*-


x1, y1 = eval(input("请输入坐标值："))
x2, y2 = eval(input("请输入坐标值："))

import turtle as tl
tl.penup()

tl.goto(x1, y1)
tl.write(str(x1) + (",") + str(y1))
# tl.write("(" + str(x1) + (",") + str(y1) ")")
tl.pendown()

tl.goto(x2, y2)
tl.write(str(x2) + (",") + str(y2))

tl.penup()
tl.goto((x1 + x2) / 2, (y1 + y2) / 2)
tl.pendown()
middel = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
tl.write(middel)


tl.done()
