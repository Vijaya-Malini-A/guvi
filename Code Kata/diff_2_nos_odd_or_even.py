m, n = map(int,raw_input().split())
if m < n:
  m, n = n, m
if (m-n)%2 != 0:
  print "odd"
else:
  print "even"
