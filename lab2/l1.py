a=input()
f=[]
for i in a:
    if len(f)==0:
        f.append(i)
    elif i=='(' or i=='{' or i=='[':
        f.append(i)
    elif i==')' and f[-1]=='(':
        f.pop()        
    elif i=='}' and f[-1]=='{':
        f.pop()
    elif i==']' and f[-1]=='[':
        f.pop()
    else:
        f.append(i)
if len(f)==0:
    print("Yes")
else:
    print("No")