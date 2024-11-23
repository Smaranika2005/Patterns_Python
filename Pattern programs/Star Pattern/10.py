a=0
for i in range(1,5):
    for j in range(i,5):
        print(" ",end="")
    print("*",end="")
    if a>0:
        print(" "*((2*a)-1),end="")
    a=a+1
    if i>1:
       print("*")
    print("\n")
print("*"*9)
    
