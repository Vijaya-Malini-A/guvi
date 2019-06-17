l, r = list(map(int,input().split()))
count = 0
for i in range(1,101):
  if i*i >= l and i*i <= r:
    count += 1
print(count)
