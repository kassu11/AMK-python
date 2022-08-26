hyttiluokka = input("Kerro hyttiluokka(LUX, A, B, C): ").lower()

if hyttiluokka == "lux":
  print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "a":
  print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "b":
  print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "c":
  print("C on ikkunaton hytti autokannen alapuolella.")
else:
  print("Valitsemasi hyttiluokka puuttuu valikoinnistamme")