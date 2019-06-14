m, n= map(int,raw_input().split())
n1, n2 = m, n
while m != n:
  if m>n:
    m = m - n
  else:
    n = n - m
if m == 0:
  gcd = n
else:
  gcd = m
print (n1*n2)/gcd
