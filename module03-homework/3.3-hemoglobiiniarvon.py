print("Laskemme onko sinun hemoglobiiniarvosi kunnossa")
sukupuoli = input("Kirjoita sukupuolesi (n/m): ").lower()
arvo = float(input("Kirjoita hemoglobiiniarvosi (g/l): "))

if sukupuoli == "n":
  if arvo < 117:
    print("Hemoglobiiniarvosi on alhainen")
  elif arvo <= 175:
    print("Hemoglobiiniarvosi on normaali")
  else:
    print("Hemoglobiiniarvosi on korkea")
elif sukupuoli == "m":
  if arvo < 134:
    print("Hemoglobiiniarvosi on alhainen")
  elif arvo <= 195:
    print("Hemoglobiiniarvosi on normaali")
  else:
    print("Hemoglobiiniarvosi on korkea")
else: print("Emme tue sukupuoltasi :D")