#2.7（计算年数和天数），提示用户输入分钟数，将分钟转换为年数和天数并显示。一年=365天




# Obtain input
minutes = eval(input("Enter the number of minutes: "))

numberOfDays = minutes // (24 * 60)
numberOfYears = numberOfDays // 365

# Display results
print(minutes, "minutes is approximately",
    numberOfYears, "years and", numberOfDays % 365, "days")