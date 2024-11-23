print("*"*9)
a=3
for i in range(1,5):
    for j in range(0,i):
        print(" ",end="")
    print("*",end="")
    if a>0:
        print(" "*((2*a)-1),end="")
    a=a-1
    if i<4:
       print("*")
    print("\n")