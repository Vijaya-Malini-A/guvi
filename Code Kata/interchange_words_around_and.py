s = list(map(str,input().split()))
if len(s) == 1 or len(s) == 2:
  for i in range(len(s)):
    print(s[i],end=" ")
else:
  for i in range(1,len(s)):
    if s[i] == "and":
      s[i-1], s[i+1] = s[i+1], s[i-1]
  for i in range(len(s)):
    print(s[i],end=" ")
