n = int(input())
li = list(map(int,input().split()))
m = []
s = 0
for i in range(n-1):
  m.append(max(li[i],li[i+1]))
for i in range(n-1):
  s += m[i]
print(s)
