a=1
for i in range(1,6,):
    for j in range(i,(i+a)):
        print(j,end="")
    a=a+1
    print("\n")