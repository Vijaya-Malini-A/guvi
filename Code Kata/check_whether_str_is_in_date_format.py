s = input()
if len(s) is 10 and s[2] is '/' and s[5] is '/':
  dd = int(s[:2])
  mm = int(s[3:5])
  yy = int(s[6:])
  if dd >= 1 and dd <= 31 and mm >= 1 and mm <= 12:
    print("yes")
  else:
    print("no")
else:
  print("no")
