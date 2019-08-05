n = int(input())
li = list(map(int,input().split()))
unique = []
for i in range(n):
  if li[i] not in unique:
    unique.append(li[i])
if len(unique) == n:
  print("unique")
else:
  for i in range(len(unique)):
    if li.count(unique[i]) > 1:
      print(unique[i],end = " ")
