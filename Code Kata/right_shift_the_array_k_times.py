n, k = map(int,raw_input().split())
li = map(int,raw_input().split())
for i in range(k):
  t = li[-1]
  for j in range(len(li)-2,-1,-1):
    li[j+1] = li[j]
  li[0] = t
for i in range(len(li)):
  print li[i],
