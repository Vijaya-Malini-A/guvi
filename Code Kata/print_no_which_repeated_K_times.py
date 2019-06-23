n, k = list(map(int,input().split()))
li = list(map(int,input().split()))
s1 = ""
for i in range(len(li)):
  if li.count(li[i]) == k and str(li[i]) not in s1:
    s1 += str(li[i])
    print(li[i],end = " ")
