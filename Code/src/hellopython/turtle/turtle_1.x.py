# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 09:26:54 2020

@author: xjy
"""


#第一章作业中出现的一些简单绘制
#运行时需要取消相应的注释

import turtle as tl

    #1.12(a)绘制正方形


# tl.penup()
# tl.goto(-100, 0)
# tl.pendown()
# tl.forward(200)

# tl.penup()
# tl.goto(0, 100)
# tl.pendown()
# tl.right(90)
# tl.forward(200)

# tl.penup()
# tl.goto(100, 100)
# tl.pendown()
# for i in range(0,4):
        
#     tl.forward(200)
#     tl.right(90)

# tl.done()

    #1.12(b)绘制十字

# tl.penup()
# tl.goto(-100, 0)
# tl.pendown()
# tl.forward(200)

# tl.penup()
# tl.goto(0, 100)
# tl.pendown()
# tl.right(90)
# tl.forward(200)

# tl.done()

    #1.12(c)绘制三角形

# tl.right(60)
# tl.forward(100)
# tl.right(120)
# tl.forward(100)
# tl.right(120)
# tl.forward(100)

# tl.done()

    #1.12(d)绘制两个三角形
# tl.right(60)
# tl.forward(100)
# tl.right(120)
# tl.forward(100)
# tl.right(120)
# tl.forward(200)
# tl.left(120)
# tl.forward(100)
# tl.left(120)
# tl.forward(100)

# tl.done()

    # 1.16(c)绘制五角星
# tl.write("start point")
# tl.right(75)
# tl.forward(300)
# tl.right(144)
# tl.forward(300)
# tl.right(144)
# tl.forward(300)
# tl.right(144)
# tl.forward(300) 
# tl.right(144)
# tl.forward(300)   


# tl.done()


    #参考答案
# import turtle

# turtle.penup()
# turtle.goto(0, 100 / 2)
# turtle.pendown()

# turtle.right(72)
# turtle.forward(100)

# turtle.right(144)
# turtle.forward(100)

# turtle.right(144)
# turtle.forward(100)

# turtle.right(144)
# turtle.forward(100)

# turtle.right(144)
# turtle.forward(100)

# turtle.done()



    #1.19绘制多边形、立方体、时钟
# tl.write("六边形")
# for i in range(0, 6):
#     tl.forward(100)
#     tl.right(60)
    
# tl.done()

    # tl.write("立方体")
# tl.forward(200)
# tl.right(90)
# tl.forward(50)
# tl.right(90)
# tl.forward(200)
# tl.right(90)
# tl.forward(50)

# tl.penup()
# tl.color("blue")
# tl.goto(75, 25)
# tl.pendown()
# tl.right(90)
# tl.forward(200)
# tl.left(90)
# tl.forward(50)
# tl.left(90)
# tl.forward(200)
# tl.left(90)
# tl.forward(50)

# tl.color("red")
# tl.goto(0, -50)

# tl.penup()
# tl.goto(0,0)
# tl.pendown()
# tl.goto(75,75)
# tl.penup()
# tl.goto(275, 75)
# tl.pendown()
# tl.goto(200, 0)
# tl.penup()
# tl.goto(200, -50)
# tl.pendown()
# tl.goto(275, 25)

# tl.done()

    # 参考答案
# import turtle

# turtle.penup()
# turtle.goto(-50, -50)
# turtle.pendown()

# turtle.goto(50, -50)
# turtle.goto(50, 0)
# turtle.goto(-50, 0)
# turtle.goto(-50, -50)

# turtle.goto(-25, -25)
# turtle.goto(100 -25, -25)
# turtle.goto(100 -25, 50 -25)

# turtle.goto(-25, 50 -25)
# turtle.goto(-25, -25)

# turtle.penup()
# turtle.goto(50, -50)
# turtle.pendown()
# turtle.goto(100 -25, -25)
        
# turtle.penup()
# turtle.goto(-50, 0)
# turtle.pendown()
# turtle.goto(-25, 25)
      
# turtle.penup()
# turtle.goto(100 -25, 25)
# turtle.pendown()
# turtle.goto(100-25 - 25, 25 - 25)
      
# turtle.hideturtle()

# turtle.done()


    #1.21时钟

    #参考答案
import turtle

turtle.color("green")
turtle.goto(-50, 0)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("blue")
turtle.goto(60, 0)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("red")
turtle.goto(0, 70)

turtle.color("black")
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(-5, 85)
turtle.pendown()
turtle.write(12)
      
turtle.penup()
turtle.goto(90, 0)
turtle.pendown()
turtle.write(3)

turtle.penup()
turtle.goto(-95, 0)
turtle.pendown()
turtle.write(9)

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.write(6)

turtle.penup()
turtle.goto(-15, -115)
turtle.pendown()
turtle.write("9:15:00")

turtle.hideturtle()

turtle.done()


















