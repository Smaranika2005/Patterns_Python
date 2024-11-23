for i in range(5,-1,-1):
    for j in range(5,i,-1):
        print(j,end="")
    for k in range(i+1,1,-1):
        print((i+1),end="")
    print("\n")
