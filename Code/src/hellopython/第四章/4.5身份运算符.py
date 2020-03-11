#身份运算符：is:用来判断二者是否地址一致，是否公用一个地址
num1 = 3
num2 = 3

print(id(num1), id(num2))
#python存储的是变量地址

# num2 = 4
# if id(num1) == id(num2):
if num1 is num2:

    print("二者地址一致")
else:
    print("二者地址不一致")

print("----------------------------------------------")

if num1 is not num2:

    print("二者地址不一致")
else:
    print("二者地址一致")
