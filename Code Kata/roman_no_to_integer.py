s = raw_input()
x = 0
for i in range(len(s)-1):
  if s[i] is 'I':
    x += 1
  elif s[i] is 'V':
    x += 5
  elif s[i] is 'X':
    x += 10
if s[-1] is 'I':
  x += 1
elif s[-1] is 'V':
  x += 5
elif s[-1] is 'X':
  x += 10
if s == "IV":
  x = 4
elif s == "IX":
  x = 9
elif s == "XIV":
  x = 14
elif s == "XIX":
  x = 19
print x
