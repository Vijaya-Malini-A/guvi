s = input()
s1, s2 = [], []
s3 = ""
for i in range(0,len(s)-1,2):
  s1.append(s[i])
  s2.append(s[i+1])
for i in range(len(s1)):
  for j in range(int(s2[i])):
    s3 += s1[i]
print(s3)
