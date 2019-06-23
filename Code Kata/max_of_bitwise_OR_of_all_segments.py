n = int(input())
li = list(map(int,input().split()))
l = []
for i in range(n):
  for j in range(0,n):
    l.append(li[i] | li[j])
print(max(l))
