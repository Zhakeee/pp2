a=int(input())
for i in range(0,a,1):
    for j in range(0,a,1):
        if i==0:
            print(j,end=" ")
        elif j==0:
            print(i,end=" ")
        elif i == j:
            print(i*j,end=' ') 
        else:
            print(0,end=" ")
    print()