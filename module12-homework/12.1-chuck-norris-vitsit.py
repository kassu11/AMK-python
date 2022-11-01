import requests

try:
  vastaus = requests.get("https://api.chucknorris.io/jokes/random")
  if vastaus.status_code == 200:
    print(vastaus.json()["value"])
  else:
    print("Vastaus ei saatu")
except:
  print("Vastaus ei saatu")