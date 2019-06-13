n = int(raw_input())
li = map(int,raw_input().split())
li.sort()
print li[len(li)//2]
