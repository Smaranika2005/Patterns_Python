a=1
for i in range(5,0,-1):
    for j in range(a,0,-1):
        print(j,end="")
    for k in range(2,(i+1)):
        print(k,end="")
    a=a+1
    print("\n")