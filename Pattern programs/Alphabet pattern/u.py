for i in range(1,6):
    a=65
    for k in range(i,5):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(a),end="")
        a=a+1
    b=a-2
    for l in range(i,1,-1):
        print(chr(b),end="")
        b=b-1
    print("\n")