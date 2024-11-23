a=1
b=1
for i in range(1,6):
    for j in range(1,b+1):
        print(a,end="")
        a=a+1
        if a>9:
            a=1
    b=b*2
    print("\n")