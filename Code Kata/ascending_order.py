n = int(raw_input())
li = map(int,raw_input().split())
for i in range(len(li)-1):
  if li[i] > li[i+1]:
    print i
    break
