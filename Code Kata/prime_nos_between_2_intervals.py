m, n = map(int,raw_input().split())
for i in range(m+1,n):
  if i>1:
    for j in range(2,i):
      if i%j == 0:
        break
    else:
      print i,
