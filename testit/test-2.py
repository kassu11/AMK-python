def wrapper(func):
  print("wrapper")
  def inner(x):
    print("inner")
    return func(x) ** 2
  return inner


@wrapper
def test_wrapper(x):
  print("test_wrapper")
  return x * 2

print(test_wrapper(2))