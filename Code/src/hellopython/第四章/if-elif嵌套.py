#高考段位
score = eval(input("请输入您的高考得分： "))

if score > 750 and score < 0:
    print("输入有误")
elif score > 700 and score <= 750:
    print("清北")
elif score > 600 and score <= 700:
    print("985")
elif score > 550 and score <= 600:
    print("211")
elif score > 500 and score <= 550:
    print("一本")
elif score > 400 and score <= 500:
    print("二本")
elif score > 300 and score <= 400:
    print("三本")
else:
    print("大专")