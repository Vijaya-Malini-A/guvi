n = int(input())
li = list(map(int,input().split()))
arr = []
for i in range(n):
  s = 0
  for j in range(i+1):
    s += li[j]
  arr.append(s)
arr1 = []
for i in range(n,-1,-1):
  s = 0
  for j in range(i):
    s += li[j]
  arr1.append(s)
for i in range(n):
  print(arr[i]+arr1[i],end = " ")
