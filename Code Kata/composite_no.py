n = int(raw_input())
if n>1:
  for i in range(2,n):
    if n%i == 0:
      print "yes"
      break
  else:
    print "no"
else:
  print "yes"
