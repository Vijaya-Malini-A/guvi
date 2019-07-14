import math
a, b = list(map(int,input().split()))
if a <= 100:
  a = math.factorial(a)
else:
  a = 0
if b <= 100:
  b = math.factorial(b)
else:
  b = 0
while a != 0 and b != 0:
  if a > b:
    a -= b
  else:
    b -= a
if a == 0:
  print(b)
else:
  print(a)
