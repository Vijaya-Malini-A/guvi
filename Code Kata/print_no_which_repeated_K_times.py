n, k = list(map(int,input().split()))
li = list(map(int,input().split()))
s = ""
for i in range(len(li)):
  if li.count(li[i]) == k and str(li[i]) not in s:
    s += str(li[i])
    print(li[i],end = " ")
