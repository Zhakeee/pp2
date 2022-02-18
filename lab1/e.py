a,b=input().split()
sum=0
if a>1:
    for i in range(2,int(a/2)+1):
        if a%i==0:
            sum=sum+1  


if sum==0 and a<500 and b%2==0:

    print ('Good job!')
else: 
    print('Try next time!')
