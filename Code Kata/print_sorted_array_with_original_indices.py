n = int(input())
li = list(map(int,input().split()))
li1 = li[:]
li.sort()
ind = []
for i in range(n):
  indi = li.index(li1[i])
  ind.append(indi)
for i in range(n):
  print(ind[i]+1,end = " ")
