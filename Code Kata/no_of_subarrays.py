n = int(input())
li = list(map(int,input().split()))
sub = 0
for i in range(n):
  for j in range(i,n):
    sub += 1
print(sub)
