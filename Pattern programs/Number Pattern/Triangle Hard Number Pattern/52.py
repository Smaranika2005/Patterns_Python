m=3
for i in range(1,6):
    if i<=3:
        for j in range(1,i+1):
            print(i,end="")
    else:
        for j in range(1,i+1):
            print((m-1),end="")
        m=m-1
    print("\n")