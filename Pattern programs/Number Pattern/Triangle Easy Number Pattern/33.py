a=5
for i in range(5,0,-1):
    for j in range(i,(i+a)):
        print(j,end="")
    a=a-1
    print("\n")