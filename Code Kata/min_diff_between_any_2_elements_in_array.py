n = int(input())
li = list(map(int,input().split()))
diff = []
for i in range(n-1):
  for j in range(i+1,n):
    if abs(li[i]-li[j]) != 0:
      diff.append(abs(li[i]-li[j]))
print(min(diff))
