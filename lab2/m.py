d=[]
while(True):
    a=input()
    if len(a)!=1:
        f,g,h=a.split()
    else: 
        break
    d.append((h,g,f))
d.sort()

for i in d: 
    x,y,z=i    
    print(z,y,x)