f=open("file.txt", "r")
cnt=0
myFile=f.read().split("\n")
for i in myFile:
    if i:
        cnt+=1
print(cnt)