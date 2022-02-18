def filter_prime(x):
    answer=[]
    for i in x:
        pravilno=True
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                pravilno=False
                break
        if pravilno:
            answer.append(i)
    return answer
print(filter_prime(list(map(int,input().split()))))