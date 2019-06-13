n = int(raw_input())
li = map(int,raw_input().split())
sum = 0
for i in range(len(li)):
  sum += li[i]
print sum / n
