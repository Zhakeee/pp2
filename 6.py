import string
chars=string.ascii_lowercase
f=open("demofile2", "w")
for i in chars:
    f.write(i)
f=open("demofile2", "r")
print(f.read())