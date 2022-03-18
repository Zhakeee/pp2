import re
def deff3(a):
    s = "^[a-z]+_.*[a-z]+$"
    x = re.search(s, a)
    if x:
        return True
    else:
        return False

s = input()
print(deff3(s))