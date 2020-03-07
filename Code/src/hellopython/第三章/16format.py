print(format(12.3212, "20.8f"))
print(format(11111112.321, "20.8f"))
print(format(12.3212312, "<20.8f"))
print(format(12.2, "20.8f"))
print(format(112321312122.2, "20.8f"))


#"20.8f":
    #20代表总体宽度
    #.8表示保留小数点后8位
    #f表示float型

    #<:左对齐
    #默认为右对齐


#"16d"
    #d表示整数


#e表示科学计数法
print("-----------------------------------------------------------------------")
print(format(54.12321312312, "<30.2e"))
print(format(0.0000000002312, "<30.2e"))
print(format(9999999999.2312, "<30.2e"))
print(format(520, "<30.2e"))
print(format(12, "<30.2e"))

print("-----------------------------------------------------------------------")
print(format(1, "10d"))
# print(format("1", "10d"))
print(format("1", "10s"))

print("\n")
print(type(format("1", "10s")))