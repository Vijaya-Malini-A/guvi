n = int(input())
li = list(map(int,input().split()))
diff = []
for i in range(n-1):
  for j in range(i,n):
    diff.append(abs(li[i]-li[j]))
print(max(diff))
