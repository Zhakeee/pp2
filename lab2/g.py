n = int(input())
d = {}
for i in range(n):
  dem, di = input().split()
  if di not in d:
    d[di] = 1
  else:
    d[di] = d[di] + 1
m = int(input())
for i in range(m):
  hunter, ability, k = input().split()
  k = int(k)
  if ability in d:
    if d[ability] - k < 0:
      d[ability] = 0
    else:
      d[ability] = d[ability] - k
print('Demons left:', sum(list(d.values())))