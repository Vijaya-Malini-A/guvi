n, m = list(map(int,input().split()))
li = list(map(int,input().split()))
s1 = li[:n]
s2 = li[n:]
s = []
for i in range(len(s1)):
  if s1[i] in s2:
    s.append(s1[i])
s.sort()
for i in range(len(s)):
  print(s[i],end = " ")
