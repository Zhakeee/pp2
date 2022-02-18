s=input()
c=input()
an1=s.find(c)
an2=s.rfind(c)
if an1!=an2:
    print(an1,an2)
else: 
    print(an1)
