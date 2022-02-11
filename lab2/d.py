a=int(input())
for i in range(1,a+1,1):
    for j in range (0,a,1):
        if(a%2==1):
            if i+j>=a:
                print("#",end ='')
            else:
                print(".",end='')
        else:
            if j+1<=i:
                print('#',end='' )
            else:
                print('.' , end='')    
    print()