#2.6(对一个整数中的各位数字求和)编写一个程序，读取一个0到1000之间的整数并计算它各位数字之和。
#例如：932，9+3+2=14
#提示：使用%（取余，得到余数）来提取数字
#      使用//（整除）运算符去除掉被提取的数字。
#       932 % 10 = 2, 932 // 10 = 93



# num = eval(input("Enter a number between 0 and 1000: "))
# p1 = num // 100#9
# p2 = (num -p1 * 100) // 10 #3
# p3 = (num -p1 * 100 - p2 * 10) // 1#2
# print(p1, p2, p3)
# print("The sum of the digits is ", p1 + p2 + p3)


#程序可以有多种设计方式与运行过程，这时就要比较二者或者多种方案中，性能好的那个。
#怎么比较性能问题，计算量与时间复杂度，是常见的两种评判标准
#常见于leetcode中
#比较方法，待后续深入学习
#从程序的实现到程序的性能提升，是一个菜鸟程序员到入门程序员的必经之路。


    #官方答案
    #  Read a number
number = eval(input("Enter an integer between 0 and 1000: "))

lastDigit = number % 10
remainingNumber = number // 10
secondLastDigit = remainingNumber % 10

remainingNumber = remainingNumber // 10
thirdLastDigit = remainingNumber % 10

# Obtain the sum of all digits
sum = lastDigit + secondLastDigit + thirdLastDigit

# Display results
print("The sum of all digits in", number, "is", sum)