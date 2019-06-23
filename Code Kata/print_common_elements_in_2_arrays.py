n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = ""
for i in range(len(a)):
  if a[i] in b and str(a[i]) not in s:
    s += str(a[i])
    print(a[i],end = " ")
