s = input()
s = s[::-1]
s1 = ""
for i in range(len(s)):
  s1 += s[i] + '-'
print(s1[:-1])
