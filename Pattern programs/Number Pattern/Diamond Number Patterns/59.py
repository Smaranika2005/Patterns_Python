a=7
for i in range(1,6):
    for j in range(1,i+1):
        if j==i:
            print(j,end="")
        else:
            print(" ",end="")
    for j in range(a,0,-1):
        print(" ",end="")
    a=a-2
    if i<5:
        print(i,end="")
    print("\n")
a=1
for i in range(4,0,-1):
    for j in range(1,i+1):
        if j==i:
            print(j,end="")
        else:
            print(" ",end="")
    for k in range(1,a+1):
        print(" ",end="")
    a=a+2
    print(i,end="")
    print("\n")
    
