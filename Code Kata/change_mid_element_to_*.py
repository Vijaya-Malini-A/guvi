s = raw_input()
if len(s)%2 == 0:
  print s[:len(s)//2-1] + '**' + s[len(s)//2+1:]
else:
  print s[:len(s)//2] + '*' + s[len(s)//2+1:]
