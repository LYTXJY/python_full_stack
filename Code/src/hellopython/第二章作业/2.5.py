#2.5(财务应用程序：计算小费)编写一个读取小技和抽筋率然后计算小费以及合计金额的程序
#例如：键入小计10，酬金率是15%，程序就会显示小费1.5，合计金额是11.5。
subtotal, gratuity = eval(input("Enter the subtotal and a gratuity rate:"))
print("The gratuity is %.2f and the total is %.2f" % (gratuity / 100 * subtotal, gratuity / 100 * subtotal + subtotal))