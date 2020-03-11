import os

cmd = input("请输入中文计算机指令：")
if cmd == "关机":
    os.system("shutdown -s -t 200")
else:
    pass
print("game over")