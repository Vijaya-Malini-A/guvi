n = int(input())
if n >= -32767 and n <= 32767:
  print("INT")
elif n >= -2147483647 and n <= 2147483647:
  print("LONG")
elif n >= -9223372036854775807 and n <= 9223372036854775807:
  print("LONG LONG")
