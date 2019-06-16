l, r = map(int,raw_input().split())
for i in range(1,100001):
  if i%l==0 and i%r==0:
    print i
    break
