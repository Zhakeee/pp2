a=input().split()
answer1=[]
answer2=[]


for i in a:
    if i>='A' and i<'[':
        answer1.append(i)
    if i>='a' and i<'{':
        answer2.append(i)
answer1.sort()
answer2.sort()
print(len(answer1)+len(answer2))
for i in answer1:

    if i[-1]==',' or i[-1]=='!' or i[-1]=='?' or i[-1]=='.' :
        print(i[:-1])
    else:
        print(i)
for i in answer2:
   
    if i[-1]==',' or i[-1]=='!' or i[-1]=='.' or i[-1]=='?':
        print(i[:-1])
    else:
        print(i)