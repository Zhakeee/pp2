import re
def text(a):
    b = 'ab{2,3}'
    x = re.search(b, a)
    if x:
        return True
    else:
        return False

a = input()
print(text(a))  