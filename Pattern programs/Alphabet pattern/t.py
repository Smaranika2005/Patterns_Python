a=65
for i in range(1,6):
    for k in range(i,5):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(a),end="")
    a=a+1
    print("\n")