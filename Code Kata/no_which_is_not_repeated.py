n = int(raw_input())
li = map(int,raw_input().split())
count = []
for i in range(len(li)):
  count.append(li.count(li[i]))
for i in range(len(count)):
  if count[i] is 1:
    print li[i]
