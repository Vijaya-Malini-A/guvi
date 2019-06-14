s = raw_input()
li = list(s)
s1 = ""
li.sort()
for i in range(len(li)):
  s1 += li[i]
print s1
