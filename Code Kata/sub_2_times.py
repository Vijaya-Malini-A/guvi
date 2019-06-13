hh1, mm1 = map(int,raw_input().split())
hh2, mm2 = map(int,raw_input().split())
if hh1 < hh2:
  hh1, hh2 = hh2, hh1
if mm1 < mm2:
  mm1, mm2 = mm2, mm1
hh = hh1 - hh2
mm = mm1 - mm2
while mm > 60:
  hh += 1
  mm -= 60
print hh,mm
