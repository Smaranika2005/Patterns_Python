for i in range(1,6):
    for j in range(1,6):
        if i%2==1:
            if j%2==1:
                print("1",end="")
            else:
                print("0",end="")
        else:
            if j%2==1:
                print("0",end="")
            else:
                print("1",end="")
    print("\n")
