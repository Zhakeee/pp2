def gen5(dano):
    for i in range(dano+1):
        yield dano-i
dano=int(input())
for i in gen5(dano):
    print(i)