s = list(map(str,input().split()))
l = []
for i in range(len(s)):
  l.append(len(s[i]))
ind = l.index(max(l))
print(s[ind])
