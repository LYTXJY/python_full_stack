import os
mystr1 = "note"
mystr2 = "pad"

os.system(mystr1+mystr2)


mystr3 = r"F:\xjy_accumulate\bilibili\python600_full_stack\Code\src\hellopython\第三章\1.txt"
mystr4 = "F:\\xjy_accumulate\\bilibili\\python600_full_stack\\Code\\src\\hellopython\\第三章\\1.txt"
mystr5 = "F:\\xjy_accumulate\\bilibili\\python600_full_stack\\Code\\src\\hellopython\\第三章\\"

os.system(mystr1 + mystr2 + " " + mystr3)
os.system(mystr1 + mystr2 + " " + mystr4)
os.system(mystr1 + mystr2 + " " + mystr5 + str(1) + ".txt")
