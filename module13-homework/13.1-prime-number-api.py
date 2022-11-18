from flask import Flask

app = Flask(__name__)
@app.route("/alkuluku/<numero>")
def alkuluku(numero):
  num = int(numero)
  maxNum = round(num / 2)
  for i in range(2, maxNum):
    if num % i == 0:
      return {"Number": num, "isPrime": False}
  return {"Number": num, "isPrime": True}


if __name__ == "__main__":
  app.run(use_reloader=True, port=5000)