for i in range(1,9):
    for j in range(i,9):
        print("*",end=" ")
    for k in range(1,2*(i-1)+1):
        print("-",end=" ")
    for k in range(i,9):
        print("*",end=" ")
    print("\n")