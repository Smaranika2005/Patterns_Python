
a=1
for i in range(1,6):
    if i % 2 == 1:
        for j in range(i):
            print(a, end=' ')
            a=a+1
    else:  
        b = a + i - 1
        for j in range(i):
            print(b, end=' ')
            b=b-1
        a=a+i
    print()
