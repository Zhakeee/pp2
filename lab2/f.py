d={}
a=int(input())
for i in  range(a):
    b,c=input().split()
    if b in d:
        d[b]+=int(c)
    else:
        d[b]=int(c)

max=0
answer=[]
for i in d:
    answer.append(i)
    if max<=d[i]:
        max=d[i]
answer.sort()
for i in answer:
    if d[i] == max:
        print(i+' is lucky!')
    else:
        print(i+' has to receive ',max-d[i],' tenge')