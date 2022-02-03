a1=int(input())
a2=input()
if a2=='k':
    a3=input()
    b = "{:."+a3+"f}"
    print(b.format(a1/1024))
else:
    print(a1*1024)