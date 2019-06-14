n, k = map(int,raw_input().split())
li = map(int,raw_input().split())
li1 = ""
for i in range(len(li)):
  if li[i]%2 != 0:
    li1 += str(li[i])
print li1[k-1]
