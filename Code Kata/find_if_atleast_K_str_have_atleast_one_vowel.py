n, k = list(map(int,input().split()))
x = 0
for i in range(n):
  s = input()
  if 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s:
    x += 1
    continue
if x >= k:
  print("yes")
else:
  print("no")
