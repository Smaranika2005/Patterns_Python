b=1
a=1
for i in range(1,6):
    for j in range(i,0,-1):
        print(b,end=" ")
        b=b+a
        a=a+1
    print("\n")