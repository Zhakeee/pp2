<<<<<<< HEAD
def gen5(dano):
    for i in range(dano+1):
        yield dano-i

dano=int(input())
for i in gen5(dano):
=======
def gen5(dano):
    for i in range(dano+1):
        yield dano-i

dano=int(input())
for i in gen5(dano):
>>>>>>> e3126c934e6fb21f6e6cb2e91055cf2f6849caef
    print(i)