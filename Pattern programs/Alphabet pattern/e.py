a=1
for i in range(65,70):
    b=i+a
    for j in range(i,b):
        print(chr(j),end="")
    a=a+1
    print("\n")