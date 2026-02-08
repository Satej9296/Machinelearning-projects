import requests
import pandas as pd

API_KEY = "ec1f042243aede5b93f02eb41510a67d"
CITY = "Pune"

URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

dates = []
temperature = []
humidity = []

for item in data["list"]:
    dates.append(item["dt_txt"])
    temperature.append(item["main"]["temp"])
    humidity.append(item["main"]["humidity"])

df = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature,
    "Humidity": humidity
})

df.to_csv("weather_data.csv", index=False)

print("Weather data fetched successfully!")
