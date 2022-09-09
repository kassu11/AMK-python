import random


def create_lottery_row():
  lotto_string = ""
  for i in range(7):
    lotto_string += str(random.randint(1, 39))

  return lotto_string



print(create_lottery_row())