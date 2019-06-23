n = int(input())
n = str(n)
f = 0
if len(n) > 1:
  for i in range(len(n)-1):
    for j in range(i+1,len(n)):
      if n[i] == n[j]:
        f = 1
if f == 1:
  print("yes")
else:
  print("no")
