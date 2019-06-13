n = int(raw_input())
n = str(n)
for i in range(len(n)):
  if int(n[i])%2 != 0:
    print n[i],
