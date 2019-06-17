s = input()
s1 = ""
for i in range(len(s)):
  if s[i].isupper():
    s1 += s[i].lower()
  elif s[i].islower():
    s1 += s[i].upper()
print(s1)
