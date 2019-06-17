n, k = list(map(int,input().split()))
nli = list(map(int,input().split()))
kli = list(map(int,input().split()))
for i in range(k):
  nli.append(kli[i])
  print(max(nli),end = ' ')
