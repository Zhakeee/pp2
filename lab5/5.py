import re
def text(a):
    b = '^a.*b$'
    if re.search(b,  a):
            return True
    else:
            return False
a = input()
print(text(a))
