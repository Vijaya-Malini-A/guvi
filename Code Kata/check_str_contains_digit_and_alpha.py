s = raw_input()
digit = "0123456789"
alpha = "abcdefghijklmnopqrstuvwxyz"
a, b = 0, 0
for i in range(len(s)):
  if s[i] in digit:
    a = 1
  elif s[i] in alpha:
    b = 1
if a == 1 and b == 1:
  print "Yes"
else:
  print "No"
