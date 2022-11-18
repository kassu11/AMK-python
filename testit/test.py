class Testi1:
  def __init__(self):
    self.a = 1
    self.b = 2

class Testi2:
  def __init__(self):
    self.c = 3
    self.d = 4

class Testi3(Testi1, Testi2):
  def __init__(self):
    Testi1.__init__(self)
    Testi2.__init__(self)


t = Testi3()
print(t.a)
print(t.b)
print(t.c)
print(t.d)