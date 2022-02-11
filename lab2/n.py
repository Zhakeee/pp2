d=[]
while(True):
    a=input()
    if a=='0':
        break
    else:
        d.append(a)
if len(d)%2==1:
    for i in range(len(d)):
        if i == len(d)/2-1:
            break
        else:
            print(int(d[i])+int(d[len(d)-i-1]))
else:
    for i in range(len(d)):
        if i == len(d)/2-1:
    
            print(d)
       print(int(d[i])+int(d[len(d)-i-1]))
