f = True
while True:
  m, n = map(int,raw_input().split())
  if m > n:
    print m - n
  else:
    print n - m
