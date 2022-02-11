x, y = map(int, input().split())
arr = []
n = int(input())
for i in range(n):
  xx, yy = map(int, input().split())
  dist = ((x-xx) * (x-xx) + (y-yy) * (y-yy)) ** (1/2)
  arr.append((dist, xx, yy))
arr.sort()
for i in arr:
  dist, xx, yy = i
  print(xx, yy)