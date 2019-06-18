s = input()
s1, s2 = "", ""
count = []
for i in range(len(s)):
  s1 += s[i].lower()
for i in range(len(s1)):
  if s1[i] not in s2 and s1[i] != " ":
    s2 += s1[i]
for i in range(len(s2)):
  count.append(s1.count(s2[i]))
mini = min(count)
for i in range(len(count)):
  if mini == count[i]:
    print(s2[i],end = " ")
