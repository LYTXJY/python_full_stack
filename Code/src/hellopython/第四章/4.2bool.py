#bool()函数中：非零为True,得零为零

print(bool(0))
print(bool(4))
print(bool(-10))
print(bool("eqw"))
print(bool([1, 2, 3]))
print(bool((1, 2, 3)))
print(bool({1:24, 2:25}))

print("\n")
print(0 == False)
print(1 == True)

print("\n")
print(bool())
print(bool(""))


if -1:
    print("-1也是真")

if "":
    print("空字符串是真")
else:
    print("空字符串是假")

if " ":
    print("空格是真")
else:
    print("空格串是假")


print("--------------------------------------------")
print(bool(" "))
print(bool(None))
