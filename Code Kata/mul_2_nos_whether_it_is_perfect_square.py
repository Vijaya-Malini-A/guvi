import math
m, n = map(int,raw_input().split())
if str(math.sqrt(m*n))[:-2].isdigit():
  print "yes"
else:
  print "no"
