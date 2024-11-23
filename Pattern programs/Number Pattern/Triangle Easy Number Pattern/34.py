a=9
for i in range(1,10,2):
    for j in range(i,(i+a),2):
        print(j,end="")
    a=a-2
    print("\n")