n = int(input())
li = list(map(int,input().split()))
li1 = li[:]
li.sort()
f = 0
for i in range(len(li)):
  if li[i] != li1[i]:
    f = 1
if f == 0:
  print("yes")
else:
  print("no")
