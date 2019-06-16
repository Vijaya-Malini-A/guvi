n = int(raw_input())
li = []
s = []
count = 1
for i in range(n):
  li.append(raw_input())
l = len(li[0])
for i in range(l):
  if li[0][i] not in s:
    s.append(li[0][i])
for i in range(1,len(li)):
  if l == len(li[i]):
    c = 0
    for j in range(len(s)):
      if li[0].count(s[j]) == li[i].count(s[j]):
        c += 1
    if c == len(s):
      count += 1
print count
