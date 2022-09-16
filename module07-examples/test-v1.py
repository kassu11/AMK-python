list_of_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

try:
  list_of_days[5] = "Saturday"
except TypeError as e:
  print("tulee errori:", e)

for day in list_of_days:
  print(day)

setti = {"Kolikko", "Sauva", "Haarniska", "Amuletti", "Kolikko", "Töppöset"}
print(setti)

setti = {(1, 2), (1, 2), (1, 2, 3)}
print(setti)
setti.add("Kolikko")
print(setti)
try:
  setti.remove(10000)
except KeyError as e:
  print("tulee errori:", e)

if "Kolikko" in setti:
  print("Kolikko löytyy")