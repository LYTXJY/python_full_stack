# 2.1（将摄氏温度转化为华氏温度）编写一个从控制台读取摄氏温度并将它转变为华氏温度并予以显示的程序。转换公式如下所示。

#看似基础，但也暗含好多知识点，比如

#格式化输出的实现方法：1是简单的print；2是更加实用的format格式
#还有就是显示位数的要求，是int，是float，还是别的格式，选项众多


#如果平时不打好基础，实际写代码时，还去菜鸟网站，进行查询，那就真的是菜鸟！

celsius = input("Rnter a degree in Celsius:")#输入摄氏温度
# print(type(celsius))#未转化的话，默认输入进来的是字符串

#int()与eval()任选其一
# celsius = int(celsius)#将输入的字符串转化为整型
# print(type(celsius))

celsius = eval(celsius)#将输入的字符串转化为整型
print(type(celsius))


fahrenheit = (9 / 5) * celsius + 32
print("%d Celsius is %f fahrenheit" % (celsius, fahrenheit))
print("%d Celsius is %.1f fahrenheit" % (celsius, fahrenheit))


#or
print(celsius, "Celsius is", fahrenheit, "Fahrenheit")


#我的问题是print的输出用法，还没掌握，只会最低级的运用，这些简单的谁还不会呢？
#一下知识补充来自菜鸟网站：https://www.runoob.com/w3cnote/python3-print-func-b.html

    #1.输出字符串和数字
print("run noob")#输出字符串
print(100)#输出数字

str = "run noob1"
print(str)#输出变量

L = [1, 2, "a"]
print(L)#输出列表

t = (1, 2, "a")
print(t)#输出元组

d = {"a":1, "b":2}
print(d)#输出字典


    #2.格式化输出整数
str = "the length of (%s) is %d" %("run noob2", len("run noob2"))
print(str)
    #3.格式化输出十六进制，十进制，八进制整数
nHex = 0xFF
print("nHex = %x, nDec = %d, nOct = %o" %(nHex, nHex, nHex))#x是16进制，d是10进制，o是8进制

    #4.格式化输出浮点数（float）
pi = 3.141592653
print("%10.3f" % pi)#字段宽为10，精度3
print("pi = %.*f" % (3, pi))#用*从后面的元组中读取字段宽度或精度

print("%010.3f" % pi)#显示的数字前面填充“0”而不是默认的空格

print("%-10.3f" % pi)#用做左对齐

print("%+f" % pi)#在正数前面显示加号( + )

    #5.自动换行
#print会自动在行末加上回车，如果不需回车，只需在print语句的结尾添加一个逗号，并设置分隔符参数end，就可以改变它的行为。
for i in range(0, 6):
    print(i)

for i in range(0, 6):
    print(i, end = " + ")#end，定义结尾输出格式与内容

for i in range(0, 6):
    print(i, end = " ")#end，定义结尾输出格式与内容


    #6.print不换行
print("\n")
for i in range(0, 3):
    print(i)#在python中默认是换行的

for i in range(0, 10):
    print(i, end = " ")#采用一个空格代替了原始print函数默认的\n，换行字符
