from time import sleep

a=int(input())
time=int(input())
sleep(time/1000)
b=a**(1/2)
print(f"Square root of  {a}   after  {time}  is  {b}")