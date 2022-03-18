def histogram(x):
    for i in x:
        print(i*"*")
histogram(list(map(int,input().split())))
