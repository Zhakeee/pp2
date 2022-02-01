s = str(input())
sum = 0
for i in s:
    sum+=ord(i)
if sum < 300 :     
    print('Oh, no!')
else :
    print('It is tasty!')