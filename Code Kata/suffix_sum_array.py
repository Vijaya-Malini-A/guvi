n = int(input())
li = list(map(int,input().split()))
arr = []
for i in range(n,-1,-1):
  s = 0
  for j in range(i):
    s += li[j]
  arr.append(s)
for i in range(n):
  print(arr[i],end = " ")
