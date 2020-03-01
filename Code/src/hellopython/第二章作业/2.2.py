#2.2（计算圆柱体的体积）编写一个读取圆柱的半径和高并利用下面的计算公式计算圆柱体底面积和体积的程序：


    #注意input返回值是字符串类型

# a = input("Enter the radius and length of a cylinder: ")
# print(a)
# print(type(a))

radius, length = eval(input("Enter the radius and length of a cylinder: "))
    #想要返回两个参数量，使用input原始返回值:字符串肯定不行，需要函数eval（）,将字符串转化为int类型
    #还要注意一点:input输入多个值时，中间需要用逗号隔开，但是这个逗号必须是英文模式下。
    # 这是外国人的程序，他们不用汉语，谢谢。
#print(radius,length)
area = radius ** 2 * 3.14159
volume = area * length
print("The area is %.4f" % (area))
print("The volume is %.1f" % (volume))


