for i in range(1,6):
    for j in range(2,((2*i)+1),2):
         print(j,end="")
    for j in range((2*(i-1)),0,-2):
            print(j,end="")
    print("\n")
