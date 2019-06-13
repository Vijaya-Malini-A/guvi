s = raw_input()
f = 0
for i in range(len(s)):
  if s[i] != '0' and s[i] != '1':
    f = 1
if f == 0:
  print "yes"
else:
  print "no"
