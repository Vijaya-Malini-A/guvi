s = input()
count = 0
for i in range(len(s)):
  if s[i] == '(':
    count += 1
  elif s[i] == ')':
    count -= 1
if count == 0:
  print("yes")
else:
  print("no")
