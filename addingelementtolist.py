list=[]
n=input("X to quit or any key to continue")
while n != "x" or n != "x":
    s=[input("input list")]
    list.append(s)
    n=input("X to quit or any key to continue")
    if n=="x" or n=="X":
        break
print(list)
