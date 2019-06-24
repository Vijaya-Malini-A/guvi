s = input().split()
x = input()
ind = 1
for i in range(len(s)):
  if s[i] == x:
    print(ind)
    break
  else:
    ind += 1
