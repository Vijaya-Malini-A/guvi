s1, s2 = list(map(str,input().split()))
f = 0
for i in range(len(s1)):
  if s1[i] in s2:
    f = 1
if f == 1:
  print("yes")
else:
  print("no")
