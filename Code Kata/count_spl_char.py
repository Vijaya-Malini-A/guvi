s = raw_input()
count = 0
for i in range(len(s)):
  if s[i] in "!@#$%^&*_(){}[]:;,./?":
    count += 1
print count
