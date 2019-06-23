n, k = list(map(int,input().split()))
n = str(n)
f = 0
for i in range(k+1):
  if str(i) not in n:
    f = 1
if f == 0:
  print("yes")
else:
  print("no")
