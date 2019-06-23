n = int(input())
li = list(map(int,input().split()))
diff = []
for i in range(len(li)):
  if li[i]%2 == 0:
    diff.append('e')
  else:
    diff.append('o')
if diff.count('e') == 1:
  ind = diff.index('e')
else:
  ind = diff.index('o')
print(li[ind])
