#变量没进行赋值，不可调用
# num#NameError :   name "num" is not defined
# print(num)


#地址问题？地址赋值

str1 = "calc"
str2 = "calc"
print(id(str1), id(str2))

str1 = "calc"
str2 = "calc2"
print(id(str1), id(str2))

#地址赋值啥意思
#在python中， 给变量赋值，   其本质是传递新的变量的地址

