for i in range(1,6):
    for j in range(1,i):
        print("",end=" ")
    for k in range(i,6):
        print("*",end=" ")
    print("\n")
for i in range(1,6):
    for j in range(i+1,6):
        print("",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print("\n")