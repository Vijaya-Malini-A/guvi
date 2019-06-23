n = int(input())
for i in range(1,n+1):
  s = str(n/i)[:-2]
  if s.isdigit():
    if int(s)%2 == 1:
      print(i)
      break
