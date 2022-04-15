def gen1(a):
    for i in range(a):
        if i <= a:
            yield i*i    
a=int(input())
#ans=gen1(a)
for i in gen1(a):
    print(i)