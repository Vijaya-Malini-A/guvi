n  = int(input())
li = list(map(int,input().split()))
li1 = []
for i in range(len(li)):
  if li[i] < n:
    li1.append(li[i])
li1.sort()
for i in range(len(li1)):
  print(li1[i],end = " ")
