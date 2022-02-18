def func(num):# как переводить с 10 -> 2 ую систему
    if num > 1:
        func(num // 2)
    print(num % 2, end='')
x=int(input())
func(x)