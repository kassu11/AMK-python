import random
import time
import os

leveys = 30
korkeus = 5;

pelaajaX = 1
pelaajaY = 1

def render():
  os.system("cls")
  for y in range(korkeus):
    if y == 0 or y == korkeus - 1:
      print("#" * leveys)
    elif y == pelaajaY + 1:
      print("#" + " " * pelaajaX + "P" + " " * (leveys - pelaajaX - 3) + "#")
    else:
      print("#" + " " * (leveys - 2) + "#")

def movePlayer():
  global pelaajaX
  global pelaajaY

  tryMovingPlayer = True
  while tryMovingPlayer:
    r = random.randint(1, 4)
    tryMovingPlayer = False
    if r == 1 and pelaajaX > 0:
      pelaajaX -= 1
    elif r == 2 and pelaajaX < leveys - 3:
      pelaajaX += 1
    elif r == 3 and pelaajaY > 0:
      pelaajaY -= 1
    elif r == 4 and pelaajaY < korkeus - 3:
      pelaajaY += 1
    else: tryMovingPlayer = True


for i in range(200):
  movePlayer()
  render()
  time.sleep(0.05)