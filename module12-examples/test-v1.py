import requests

hakusana = input("Anna hakusana: ")
pyyntö = f"https://api.tvmaze.com/search/shows?q={hakusana}"

try:
  vastaus = requests.get(pyyntö)
  if vastaus.status_code == 200:
    print("Vastaus saatu")
    tulokset = vastaus.json()
    for sarja in tulokset:
      print(sarja["show"]["name"])
  else:
    print("Vastaus ei saatu")
except:
  print("Vastaus ei saatu")