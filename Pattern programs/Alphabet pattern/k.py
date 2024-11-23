a=65
b=97
f=b
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(f),end="")
        if f==b:
            f=a
            b=b+1
            a=a+1
        else:
            f=b
            a=a+1
            b=b+1
        f=f+1
    print("\n")
