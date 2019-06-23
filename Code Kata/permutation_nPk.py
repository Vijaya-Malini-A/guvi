import math
n, k = list(map(int,input().split()))
print(int(math.factorial(n)/math.factorial(n-k)))
