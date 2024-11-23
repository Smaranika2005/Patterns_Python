for i in range(65,70):
    b=i
    a=4
    for j in range(65,i+1):
        print(chr(b),end=" ")
        b=b+a
        a=a-1
    print("\n")