<<<<<<< HEAD
def gen3(max):
    for i in range(1,max+1):
        if i % 3 == 0 and i % 4 == 0 and i > 0:
            yield i


max=int(input())
for i in gen3(max):
    print(i)
=======
def gen3(max):
    for i in range(1,max+1):
        if i % 3 == 0 and i % 4 == 0 and i > 0:
            yield i


max=int(input())
for i in gen3(max):
    print(i)
>>>>>>> e3126c934e6fb21f6e6cb2e91055cf2f6849caef
