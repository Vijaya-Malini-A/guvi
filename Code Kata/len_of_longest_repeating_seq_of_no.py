n = int(input())
li = list(map(int,input().split()))
l = []
for i in range(len(li)):
  l.append(li.count(li[i]))
print(max(l))
