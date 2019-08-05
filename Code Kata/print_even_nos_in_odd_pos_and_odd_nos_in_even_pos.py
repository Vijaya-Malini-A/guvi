n = int(input())
li = list(map(int,input().split()))
for i in range(n):
  if i%2 == 0 and li[i]%2 == 1:
    print(li[i],end=" ")
  elif i%2 == 1 and li[i]%2 == 0:
    print(li[i],end=" ")
