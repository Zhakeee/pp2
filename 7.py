import re
a = input()
x = re.split("_", a)
r = x[0] + ''.join(i.title() for i in x[1:])
print(r)