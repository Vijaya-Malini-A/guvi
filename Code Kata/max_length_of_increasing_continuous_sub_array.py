n = int(input())
li = list(map(int,input().split()))
c = 1
count = []
for i in range(n-1):
  if li[i] < li[i+1]:
    c += 1
  else:
    c = 1
    continue
  count.append(c)
print(max(count))
