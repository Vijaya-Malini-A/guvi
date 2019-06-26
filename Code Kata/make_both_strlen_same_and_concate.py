s, m = list(map(str,input().split()))
l1 = len(s)
l2 = len(m)
if l1 > l2:
  print(s[:l2]+m)
elif l1 < l2:
  print(s+m[:l1])
else:
  print(s+m)
