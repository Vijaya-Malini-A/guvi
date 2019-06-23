n = int(input())
li = list(map(int,input().split()))
s = 0
for i in range(n-1):
  s += li[i] + li[i+1]
print(s)
