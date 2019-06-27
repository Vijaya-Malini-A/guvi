n, k = list(map(int,input().split()))
li = list(map(int,input().split()))
li1 = []
for i in range(n):
  if li.count(li[i]) < k and li[i] not in li1:
    li1.append(li[i])
li1.sort()
for i in range(len(li1)):
  print(li1[i],end = " ")
