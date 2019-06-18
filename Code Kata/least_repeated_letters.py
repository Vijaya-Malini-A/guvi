s = input()
s1 = ""
count = []
for i in range(len(s)):
  if s[i] not in s1 and s[i] != " ":
    s1 += s[i]
for i in range(len(s1)):
  count.append(s.count(s1[i]))
mini = min(count)
for i in range(len(count)):
  if mini == count[i]:
    print(s1[i],end = " ")
