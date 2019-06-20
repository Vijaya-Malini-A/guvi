n, k = list(map(int,input().split()))
li = list(map(int,input().split()))
for i in range(k-1):
  li.remove(min(li))
print(min(li))
