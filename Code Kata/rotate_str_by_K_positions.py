s, k = list(map(str,input().split()))
k = int(k)
for i in range(k):
  s1 = ""
  s1 += s[-1]
  for j in range(len(s)-1):
    s1 += s[j]
  s = s1
print(s)
