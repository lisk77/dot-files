import requests

conditions = {"Clear": " ☀️ ", "Clouds": " ☁️ ", "Thunderstorm": " ⛈ ", "Drizzle": " 🌧 ", "Rain": " 🌧 ", "Snow": " 🌨 ", "Atmosphere": " 🌫 "}             
api = "https://api.openweathermap.org/data/2.5/weather?lat=51.358627&lon=12.476209&appid=aef9dce181f3ccc20a33a1fe85915da9"
data = requests.get(api).json()

condition = data["weather"][0]["main"]
temp = round(data["main"]["temp"] - 273.15)

with open("cond", "w") as cond:
    cond.write(conditions[condition])

with open("temp", "w") as tem:
    tem.write(str(temp) + "°C ")
