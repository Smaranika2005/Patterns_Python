for i in range(1,6):
    if i%2==1:
        for j in range(1,(2*i),2):
            print(j,end="")
    else:
        for j in range(2,(2*i+1),2):
            print(j,end="")
    print("\n")
