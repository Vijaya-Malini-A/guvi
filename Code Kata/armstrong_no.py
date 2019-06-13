n = int(raw_input())
temp = n
arm = 0
while n>0:
  r = n % 10
  arm = arm + (r * r * r)
  n = n / 10
if temp == arm:
  print "yes"
else:
  print "no"
