s = raw_input()
f = 0
for i in range(len(s)):
  if s.count(s[i]) != 1:
    f = 1
if f == 0:
  print "yes"
else:
  print "no"
