def squares(a,b):
    while(a<=b):
        yield a*a
        a+=1
dano=input().split()
for i in squares(int(dano[0]),int(dano[1])):
    print(i)