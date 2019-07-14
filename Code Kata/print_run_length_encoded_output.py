s = input()
s = list(s)
s1, s2 = [], []
s3 = ""
for i in range(len(s)):
  if s[i] not in s1:
    s1.append(s[i])
for i in range(len(s1)):
  s2.append(s.count(s1[i]))
for i in range(len(s1)):
  s3 += s1[i] + str(s2[i])
print(s3)
