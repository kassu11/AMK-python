koko = float(input("Kirjoita kuhasi koko (cm): "))

if koko < 37:
  print(f"Kuhasi on liian säälittävän kokoinen, laske se takaisin mereen ja kerää {37 - koko}cm pidempi kuha")
else:
  print("Kuhasi on hyvän kokoinen, hyvää työtä 👍")