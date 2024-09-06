list1=["a","a","b","a","a","d","c",1,2,3,3,3,3,3]
b=len(list1)
print(b)
n=input("enter")

for i in range(1,b):
    
    
    for x in list1:
      
      if n==x:
        list1.remove(n)
    print(i,end=" ")
    
print(list1)
