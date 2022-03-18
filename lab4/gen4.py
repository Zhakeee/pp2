<<<<<<< HEAD
def squares(a,b):
    while(a<=b):
        yield a*a
        a+=1

dano=input().split()
for i in squares(int(dano[0]),int(dano[1])):
=======
def squares(a,b):
    while(a<=b):
        yield a*a
        a+=1

dano=input().split()
for i in squares(int(dano[0]),int(dano[1])):
>>>>>>> e3126c934e6fb21f6e6cb2e91055cf2f6849caef
    print(i)