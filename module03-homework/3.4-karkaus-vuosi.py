vuosi = int(input("Kirjoita vuosi: "))

if vuosi % 4 == 0 or vuosi % 400 == 0:
  print(f"{vuosi} on karkausvuosi")
else:
  print(f"{vuosi} ei ole karkausvuosi")