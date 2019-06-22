n = int(input())
li = input()
s = []
for i in range(n-1,-1,-1):
  if li[i] is '0':
    for j in range(i):
      if li[j] != '0' and li[j] != ' ':
        s.append(li[j])
    break
for i in range(len(s)):
  print(s[i],end = " ")
