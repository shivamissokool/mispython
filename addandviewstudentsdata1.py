student=[]
name=[]
class_=[]


x=0
for x in range(1,100):
    choice=int(input("to add - 1, to view - 2 :"))
    if choice==1:
       scholarno= input("enter the scholar no: ")
       name1=input("enter the name of student:")
       name2=str(name1)
       class_1=input("enter the class no:")
       student.append([scholarno])
       name.append([name2])
       class_.append([class_1])
       print("done!")

    if choice==2:
       n=int(input("Scholar no:"))
       print("scholar Number:",student[n],"name",name[n],"class",class_[n])
