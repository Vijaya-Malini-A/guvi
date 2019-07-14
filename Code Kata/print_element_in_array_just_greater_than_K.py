n, k = list(map(int,input().split()))
li = list(map(int,input().split()))
li.sort()
for i in range(n):
  if li[i] > k:
    print(li[i])
    break
