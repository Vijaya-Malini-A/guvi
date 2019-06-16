l = int(raw_input())
s = raw_input()
s = list(s)
s1 = s[:]
s2 = ""
vowels = 'aeiouAEIOU'
for i in range(l):
  if s[i] in vowels:
    s1.remove(s[i])
s1.reverse()
for i in range(len(s1)):
  s2 += s1[i]
print s2
