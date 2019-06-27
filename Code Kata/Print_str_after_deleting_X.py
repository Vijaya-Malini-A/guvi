s = list(map(str,input().split()))
x = input()
s.remove(x)
for i in range(len(s)):
  print(s[i],end = " ")
