d=[] 
while(True): 
    a=int(input()) 
    if a==0: 
        break 
    else : 
        d.append(a) 
a = "" 
if len(d)%2==1: 
    for i in range(len(d)): 
        if i == len(d)-i-1: 
            a+=str(d[i]) 
            break 
        else: 
            a+=str(d[i]+d[len(d)-i-1]) +" " 
    print(a) 
else: 
    for i in range(len(d)): 
        if i != len(d)-i-1: 
            a+=str(d[i]+d[len(d)-i-1]) +" " 
        if a.count(' ') == (len(d)/2): 
            break 
    print(a)
