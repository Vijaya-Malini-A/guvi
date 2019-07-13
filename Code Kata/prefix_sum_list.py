n = int(input())
li = list(map(int,input().split()))
li1 = []
s = 0
for i in range(n):
  s += li[i]
  li1.append(s)
  print(li1[i],end = " ")
