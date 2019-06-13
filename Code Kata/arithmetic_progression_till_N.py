n, a, d = map(int,raw_input().split())
add = 0
for i in range(1,n+1):
  add = add + a + ((i - 1) * d)
print add
