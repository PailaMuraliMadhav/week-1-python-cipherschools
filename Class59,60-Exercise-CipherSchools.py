name=input("enter your name ")
temp_var=""
i=0
while i < len(name):
    temp_var +=name[i]
    print(f"{name[i]}:{name.count(name[i])}")
    i+=1