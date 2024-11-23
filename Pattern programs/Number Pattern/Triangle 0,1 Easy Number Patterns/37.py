a=1
for i in range(1,6):
    for j in range(i,0,-1):
        print(a,end="")
        if a==1:
            a=0
        else:
            a=1
    print("\n")
