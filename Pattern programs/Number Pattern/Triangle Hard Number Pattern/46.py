for i in range(1,6):
    if i%2==1:
        for j in range(1,i+1):
            print(j,end="")
    else:
        for j in range(i,0,-1):
            print(j,end="")
    print("\n")
