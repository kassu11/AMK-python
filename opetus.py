print("Hello World")

num = int(input("Kirjoita numero: "))

for i in range(num):
  vali = " " * (num - i - 1)
  sivut = "#" * i
  print(vali + sivut + "#" + sivut)