n, k = list(map(int,input().split()))
nli = list(map(int,input().split()))
kli = list(map(int,input().split()))
for j in range(k):
  nli.append(kli[j])
  print(max(nli),end = ' ')
