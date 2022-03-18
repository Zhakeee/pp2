import re
def camke(a):
        s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', a)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
a = input()
print(camke(a))