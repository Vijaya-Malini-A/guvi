s = raw_input()
s1 = ""
for i in range(len(s)):
  s1 += chr(ord(s[i]) + 3)
print s1
