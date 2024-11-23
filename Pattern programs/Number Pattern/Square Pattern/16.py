for i in range(1,6):
    for j in range(i,6):
        print(j,end="")
    for k in range(i,1,-1):
        print((k-1),end="")
    print("\n")