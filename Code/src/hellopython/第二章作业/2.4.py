#2.4(将磅转换为千克)编写一个将磅转换为千克的程序。这个程序体术用户输入磅数，转换为千克数并显示结果。一磅等于0.454千克。
pounds = eval(input("Enter a value in pounds: "))
print(pounds, "pounds is %.3f kilograms" % (pounds * 0.454))