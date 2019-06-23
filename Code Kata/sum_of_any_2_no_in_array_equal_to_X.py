n, x = list(map(int,input().split()))
li = list(map(int,input().split()))
f = 0
for i in range(n-1):
  for j in range(1,n):
    if li[i] + li[j] == x:
      f = 1
if f == 1:
  print("yes")
else:
  print("no")
