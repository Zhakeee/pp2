x=int(input())

for i in range(x):
    s=input()
    b=len(s)-10
    d='@gmail.com'
    if d==s[b:]:
        print(s[:b])



