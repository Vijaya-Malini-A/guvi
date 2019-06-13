n = raw_input()
f = 0
s = ""
for i in range(len(n)):
  if n[i] is '.':
    s = n[:i] + n[i+1:]
    f = 1
if f == 0:
  s = n
if s.isdigit():
  print "yes"
else:
  print "no"
