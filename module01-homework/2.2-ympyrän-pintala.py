import math

print("Lasken ympyrän pinta-alan")
sade = int(input("Kerro ympyrän säde metreinä?: "))
print(f"{sade} (m) säteisen ympyrän pinta-ala on: {(math.pi * sade ** 2):.3f} neliömetriä")