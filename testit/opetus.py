print("Hello World")

num = int(input("Kirjoita numero: "))

for i in range(num):
  vali = " " * (num - i - 1)
  sivut = "#" * i
  print(vali + sivut + "#" + sivut)

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

print(f"{bcolors.OKGREEN}test{bcolors.ENDC}{bcolors.FAIL}{bcolors.BOLD}{bcolors.UNDERLINE}:D{bcolors.ENDC}asd")