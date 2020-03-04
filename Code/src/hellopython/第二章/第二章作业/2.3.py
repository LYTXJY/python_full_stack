#2.3（将英尺数转换为米数）编写一个程序，它读取英尺数然后将它转换成米数并显示结果。一英尺等于0.305米。

feet = eval(input("Enter a value for feet: "))
print(feet, "feet is %.4f meters" % (feet * 0.305))