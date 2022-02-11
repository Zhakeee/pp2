a=int(input())
d=[]
for i in range(a):
    b=input()
    sum1=0
    sum2=0
    sum3=0
    for j in b:
        if j>='A' and j<='Z':
            sum1=sum1+1
        elif j>='a' and j<='z':
            sum2=sum2+1
        elif j>='0' and j<='9':
            sum3=sum3+1
    if sum1>0 and sum2>0 and sum3>0:
        if b in d:
            pass
        else:
            d.append(b)
print(len(d))
d.sort()
for i in d:
    print(i)
        