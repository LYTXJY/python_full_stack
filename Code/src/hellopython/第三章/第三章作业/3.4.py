# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:02:55 2020

@author: xjy
"""


#3.4

# import math
# side = eval(input("Enter the side: "))
# area = 5 * side ** 2 / (4 * math.tan(3.1415926 / 5))
# print("The area of the pentagon is %f" % area)



#参考答案

import math
side = eval(input("Enter the side: "))
# Compute the area
area = 5 * side * side / math.tan(math.pi / 5) / 4

print("The area of the pentagon is", area)
