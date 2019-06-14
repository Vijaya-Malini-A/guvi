m, n= map(int,raw_input().split())
while m != n:
  if m>n:
    m = m - n
  else:
    n = n - m
if m == 0:
  print n
else:
  print m
