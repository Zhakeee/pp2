k=input().split()
lin=[]
ans=0
if len(k)==1:
    b=int(input())
    a=int(k[0])
else :
    a=int(k[0])
    b=int(k[1])
for i in range (0,a,1):
    lin.append(b+i*2)
for i in lin:
    ans=i^ans
print(ans)