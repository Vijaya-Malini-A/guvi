s = raw_input()
s1 = ""
for i in range(len(s)):
  ascii = ord(s[i]) + 3
  if ascii == 123:
    ascii = 97
  elif ascii == 124:
    ascii = 98
  elif ascii == 125:
    ascii = 99
  elif ascii == 91:
    ascii = 65
  elif ascii == 92:
    ascii = 66
  elif ascii == 93:
    ascii = 67
  s1 += chr(ascii)
print s1
