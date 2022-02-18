def stroka(s):
    answer=s.split()
    
    return(" ".join(reversed(answer)))
print(stroka(input()))