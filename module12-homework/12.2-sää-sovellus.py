import requests

api_key = "29c498a8ebbd755ceb6b52b14d37cced"
paikkakunta = input("Anna paikkakunta: ")

try:
  vastaus = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&units=metric&appid={api_key}")
  if vastaus.status_code == 200:
    json_data = vastaus.json()
    print(f'''"{paikkakunta}" sää on: {json_data["weather"][0]["description"]}''')
    print(f'''"{paikkakunta}" lämpötila on: {json_data["main"]["temp"]}c''')
  else:
    print("Vastaus ei saatu")
except:
  print("Vastaus ei saatu")