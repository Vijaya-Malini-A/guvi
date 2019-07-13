n = int(input())
li = list(map(int,input().split()))
li1 = []
s = 0
for i in range(n):
  if i%2 != 0 or li[i]%2 == 0:
    s += li[i]
    li1.append(s)
  else:
    s += li[i]
    li1.append(li[i])
  print(li1[i],end = " ")
