n = int(input())
li = list(map(int,input().split()))
unique = []
c = 0
for i in range(n):
  if li[i] not in unique:
    unique.append(li[i])
  else:
    print(li[i])
    c = 1
    break
if c == 0:
  print("unique")
