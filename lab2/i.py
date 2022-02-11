a=int(input())
answer1=[]
sum=0
for i in range(a):
    b=input()
    if b[0]=='1':
        answer=""
        for j in range(2,len(b)):
            answer+=b[j]
        answer1.append(answer)
    if b[0]=='2':
        sum=sum+1
for i in range(sum):
    print(answer1[i],end=' ')
    