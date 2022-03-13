import re
def deff4(s):
    d='^[A-Z][a-z]'
    x=re.search(d,s)
    if x:
        return "YES"
    else:
        return "NO"
s=input()
print(deff4(s))