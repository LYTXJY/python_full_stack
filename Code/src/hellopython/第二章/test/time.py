import time

mytime = time.time()

print(mytime)
print("自从1970年1月1号起始，过去了", mytime, "秒")


#以小时，分钟，秒的格式进行输出

hours = None
minutes = None
seconds = None

#测试账号
# past_time = 365 * 24 * 60 * 60

past_time = time.time()

print(past_time)
past_time = int(past_time)
print(past_time,"秒")
hours = past_time // 3600
seconds =past_time - hours * 3600
minutes = seconds // 60
seconds = seconds - minutes * 60

print("距离1970年1月1号已经过去了",
      hours,"小时",
      minutes, "分钟",
      seconds, "秒")
#增加天与年
days = None
months = None
years = None

days = hours // 24
hours = hours % 24

months = days // 30
days = days % 30

years = months // 12
months = months % 12

print("距离1970年1月1号已经过去了",
      years,"年",
      months,"月",
      days,"天",
      hours,"小时",
      minutes, "分钟",
      seconds, "秒")





#参考答案
import time
mytime = time.time()

seconds = int(mytime) % 60 #分钟，小时都是60的整数倍，所以，不能被60整除的，就是留下来的秒
hours = int(mytime) // 3600
minutes = (int(mytime) - int(mytime) // 3600 * 3600)#剩余的秒数
minutes = (minutes - seconds) // 60
print("距离1970年1月1号已经过去了",
      hours,"小时",
      minutes, "分钟",
      seconds, "秒")
#说实话，这个例子逻辑不是很清晰，只能作为参考。
''':arg
假如时间3959秒
3959%60=59秒
3959//3600=1小时
（3959 - 1 * 3600 -59 ）//60

'''