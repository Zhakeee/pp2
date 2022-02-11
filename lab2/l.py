s=input()
sum1=0
sum2=0
sum3=0
for i in s:
    if i=='(':
        sum1=sum1+1
    if i=='[':
        sum2=sum2+1    
    if i=='{':
        sum3=sum3+1
    if i==')':
        sum1=sum1-1
    if i==']':
        sum2=sum2-1
    if i=='}':
        sum3=sum3-1
    if sum1<0:
        print("No")
        exit()
    if sum2<0:
        print("No")
        exit()
    if sum3<0:
        print("No")
        exit()
if(sum1==0 and sum2==0 and sum3==0):
    print("Yes")
else:
    print("No")