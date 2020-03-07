# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:11:34 2020

@author: xjy
"""


#3.12
#用户自行输入五角星边长

import turtle as t
length = eval(input("请输入五角星边长："))


#t.showturtle()
t.rt(72)
t.fd(length)
t.rt(144)
t.fd(length)
t.rt(144)
t.fd(length)
t.rt(144)
t.fd(length)
t.rt(144)
t.fd(length)


t.done()