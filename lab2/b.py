a=int(input())
max1=0
max2=0
x=list(map(int, input().split()))
for i in range(0,a,1):
    if x[i]>max1:
        max1=x[i]
x.remove(max1)
for i in range (0,a-1,1):
    if x[i]>max2:
        max2=x[i]
print(max1*max2) 
   