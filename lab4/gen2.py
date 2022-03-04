def gen2(max):
    for i in range(max+1):
        if i % 2  == 0 :
            yield i

max=int(input())
for i in gen2(max):
    print(i)
