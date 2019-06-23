n = int(input())
li = list(map(int,input().split()))
s = []
for i in range(n):
  if li[i] not in s:
    s.append(li[i])
for i in range(len(s)):
  print(s[i],end = " ")
