<<<<<<< HEAD
def gen1(a):
    for i in range(a):
        if i <= a:
            yield i*i
            

a=int(input())
#ans=gen1(a)
for i in gen1(a):
=======
def gen1(a):
    for i in range(a):
        if i <= a:
            yield i*i
            

a=int(input())
#ans=gen1(a)
for i in gen1(a):
>>>>>>> e3126c934e6fb21f6e6cb2e91055cf2f6849caef
    print(i)