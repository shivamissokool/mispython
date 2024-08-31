record=[]
h=int(input("number of students:"))
for x in range (0,h):
    r=input("Roll no:")
    record.append(r)
    n=input("Name:")
    record.append(n)
    c=input("Class:")
    record.append(c)
    m=input("Marks:")
    record.append(m)
b=len(record)
f=input("enter:")
for i in range(0,b):
    if record[i]==f:
        print("roll no-",record[i])
        print("name-",record[i+1])
        print("class-",record[i+2])
        print("marks-",record[i+3])
