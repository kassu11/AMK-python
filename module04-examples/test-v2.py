i = 0
while i < 10:
  i += 1
  print(i)
else: # Suorittuu kun while looppi lopettaa luonnollisesti
  print("Loppu")

i = 0
while i < 10:
  i += 1
  print(i)
  if i == 4: break
else:
  print("Loppu")