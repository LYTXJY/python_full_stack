a = "a"
#但单个字符，可以使用单引号编写
# a = 'a'
# A = 'A'

A = "A"
ab = "ab"
AB = "AB"

c = "我"

print(type(a), type(A), type(ab), type(AB))
#注意ord只能求出单个字符的ascii码值

print(ord(a))
print(ord(A))
print(ord(c))
#
#print(ord(ab))
# print(ord(AB))

#chr()函数：求码值所对应的字符
print(chr(65))
#英文字母一共26个，65+26 = 91
print(chr(97))
print(chr(25105))
#一个汉字也是一个字符

# d = "我的"
# print(ord(d))


#本质：码值表：字符与数字之间的映射，一一对应，且不重复，不冲突
#数学上，好像叫双射？




#统一码
e = "儒"
print(ord(e))
print(chr(20754))
import os
os.system("calc")
print(chr("\u5112"))