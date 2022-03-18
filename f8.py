def func_007(x):
    for i in range(len(x)-1):
        if x[i] == '0' and x[i+1]=='0' and x[i+2]=='7':
            return True
    return False
print(func_007(input().split(',')))