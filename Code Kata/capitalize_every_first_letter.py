s = map(str,raw_input().split())
for i in range(len(s)):
  s1 = ""
  s1 += s[i][0].upper()
  s1 += s[i][1:]
  print s1,
