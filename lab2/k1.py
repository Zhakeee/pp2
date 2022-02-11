a=input().split()
b=set(a)
print(len(b))
d=list(b)
d.sort()
for i in d:
    if i[-1]==',' or i[-1]=='!' or i[-1]=='?' or i[-1]=='.' :
        print(i[:-1])
    else: 
        print(i)