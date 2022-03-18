import re
def ree(a):
    s = '^a(b*)$'
    if re.search(s,a):
        return 'YES'
    else :
        return 'NO'
a=input()
print(ree(a))