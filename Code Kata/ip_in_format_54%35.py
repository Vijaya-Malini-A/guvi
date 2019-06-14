f = True
while True:
  m, op, n = map(str,raw_input().split())
  if op == '/':
    print int(m) / int(n)
  elif op == '%':
    print int(m) % int(n)
