n = int(input())
li = list(map(int,input().split()))
if len(li) > 1:
  result = li[0] | li[1]
else:
  result = li[0]
for i in range(2,n):
  result |= li[i]
print(result)
