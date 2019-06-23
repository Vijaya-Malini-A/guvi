n, m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
r = a + b
r.sort()
for i in range(len(r)):
  print(r[i],end = " ")
