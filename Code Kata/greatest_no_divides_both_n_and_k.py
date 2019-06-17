n, k = list(map(int,input().split()))
for i in range(k,0,-1):
  if n%i == 0 and k%i == 0:
    print(i)
    break
