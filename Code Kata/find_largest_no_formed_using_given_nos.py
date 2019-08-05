n = int(input())
li = list(map(int,input().split()))
li.sort()
li.reverse()
s = ""
for i in range(n):
  s += str(li[i])
print(int(s))
