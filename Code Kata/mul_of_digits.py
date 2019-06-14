n = int(raw_input())
n = str(n)
mul = 1
for i in range(len(n)):
  mul *= int(n[i])
print mul
