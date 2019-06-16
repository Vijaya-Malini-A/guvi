n = int(raw_input())
fact = []
for i in range(1,n+1):
  if n%i == 0:
    fact.append(i)
fact.sort()
for i in range(len(fact)):
  if fact[i] > 1:
    for j in range(2,fact[i]):
      if fact[i]%j == 0:
        break
    else:
      print fact[i],
