n = int(input())
n = str(n)
n = list(n)
n.sort()
n.reverse()
for i in range(len(n)):
  print(n[i],end="")
