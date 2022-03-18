def no_set(x):
    answer=[]
    for i in x:
        if i not in answer:
            answer.append(i)
    return answer
print(" ".join( no_set(input().split())))