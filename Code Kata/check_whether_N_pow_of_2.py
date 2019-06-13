n = int(raw_input())
f = 0
for i in range(100):
  if n == 2**i:
    f = 1
    print "yes"
    break
if f == 0:
  print "no"
