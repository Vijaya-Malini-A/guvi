n = int(raw_input())
t1 = 1
t2 = 1
fibo = 0
print t1,t2,
for i in range(2,n):
  fibo = t1 + t2
  t1 = t2
  t2 = fibo
  print fibo,
