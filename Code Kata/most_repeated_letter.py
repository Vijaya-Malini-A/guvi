s = raw_input()
count = []
for i in range(len(s)):
  count.append(s.count(s[i]))
ind = count.index(max(count))
print s[ind]
