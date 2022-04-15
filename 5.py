text=["programming", " principles", " II"]
f=open("file.txt", "w")
for i in text:
    f.write(i)
f.close()
f=open("file.txt", "r")
print(f.read())