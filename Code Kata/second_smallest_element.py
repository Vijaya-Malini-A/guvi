n = int(input())
li = list(map(int,input().split()))
li.remove(min(li))
print(min(li))
