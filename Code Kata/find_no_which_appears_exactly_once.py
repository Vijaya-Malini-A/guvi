n = int(input())
li = list(map(int,input().split()))
for i in range(n):
  if li.count(li[i]) == 1:
    print(li[i])
