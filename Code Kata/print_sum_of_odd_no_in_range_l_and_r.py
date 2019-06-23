l, r = list(map(int,input().split()))
res = 0
for i in range(l,r+1):
  if i%2 != 0:
    res += i
print(res)
