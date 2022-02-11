arr = list(map(int, input().split()))
jmp = 0
for i in range(len(arr)):
  if jmp < arr[i]+i:
    jmp = arr[i]+i
  if i >= jmp and i != len(arr)-1:
    print(0)
    break
else:
  print(1)