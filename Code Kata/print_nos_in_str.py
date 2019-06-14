s = raw_input()
s1 = ""
for i in range(len(s)):
  if s[i].isdigit():
    s1 += s[i]
print s1
