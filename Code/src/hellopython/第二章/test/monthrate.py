#计算利率

#月供 = 贷款数*月利率 / （1 - 1/（1+月利率）**（年限*12））

years = eval(input("请输入贷款年限："))
money = eval(input("请输入贷款金额："))
monthrate = eval(input("请输入贷款月利率："))

monthmoney = money * monthrate / (1 - 1 / (1 + monthrate) ** (years * 12))
totalmoney = monthmoney * years * 12

print("月供：", monthmoney, "总还款：", totalmoney)

