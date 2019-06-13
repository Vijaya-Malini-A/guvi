m, n = map(int,raw_input().split())
for i in range(m+1,n):
  temp = i
  arm = 0
  while i>0:
    r = i % 10
    arm = arm + (r * r * r)
    i = i / 10
  if temp == arm:
    print arm
