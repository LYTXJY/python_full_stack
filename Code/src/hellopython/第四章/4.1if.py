import os
cmd = input("cmd ")
isrun = (cmd == "notepad")
print(isrun)
if isrun:
    os.system(cmd)
