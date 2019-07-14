n, k = list(map(int,input().split()))
li = list(map(int,input().split()))
if k in li:
  print(k)
else:
  li.sort()
  for i in range(n-1,-1,-1):
    if li[i] < k:
      print(li[i])
    break
