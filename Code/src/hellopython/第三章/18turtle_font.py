import turtle as t

# t.screensize(100,100)
t.showturtle()

# t.write("切勿不自量力", font = ("华文琥珀", 10))
# t.circle(100)
# t.circle(100, extent = 180)
# t.circle(100, steps = 3)
# t.circle(100, steps = 4)
# t.circle(200, steps = 5)
# t.color("red")
# t.circle(200, steps = 18)
# t.color("green")
# t.circle(200)



#填充




t.begin_fill()
t.hideturtle()
t.circle(150)
t.color("yellow")
t.end_fill()

t.reset()#重置

t.pensize(20)
t.pu()
t.goto(-50,-50)
t.pd()
t.begin_fill()
t.circle(60, extent = 360)
t.color("blue")
t.end_fill()


t.pu()
t.goto(70,70)
t.pd()
t.colormode(255)
t.begin_fill()
t.circle(50)
t.color(127, 255, 212)
t.end_fill()



t.done()
