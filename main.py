import requests, json
timezone = "GMT"
latitude = 56.5645 #Latvia
longitude = 24.0621


def getWeatherDescription(weatherCode):
  if weatherCode == "0":
    return "Clear sky ☀️"
  elif weatherCode == "1":
    return "Mainly clear 🌤️"
  elif weatherCode == "2":
    return "Partly cloudy ⛅"
  elif weatherCode == "3":
    return "Overcast 😶‍🌫️"
  elif weatherCode == "45":
    return "Fog 🌫️"
  elif weatherCode == "48":
    return "Depositing rime fog 🌫️"
  elif weatherCode == "51":
    return "Drizzle: Light ☂️"
  elif weatherCode == "53":
    return "Drizzle: Moderate ☂️"
  elif weatherCode == "55":
    return "Drizzle: Dense intensity ☂️"
  elif weatherCode == "56":
    return "Freezing Drizzle: Light ☂️"
  elif weatherCode == "57":
    return "Freezing Drizzle: Dense intensity ☂️"
  elif weatherCode == "61":
    return "Rain: Slight 🌦️"
  elif weatherCode == "63":
    return "Rain: Moderate 🌦️"
  elif weatherCode == "65":
    return "Rain: Heavy intensity 🌧️"
  elif weatherCode == "66":
    return "Freezing Rain: Light 🌨️"
  elif weatherCode == "67":
    return "Freezing Rain: Heavy intensity 🌨️"
  elif weatherCode == "71":
    return "Snow fall: Slight ❄️"
  elif weatherCode == "73":
    return "Snow fall: Moderate ❄️"
  elif weatherCode == "75":
    return "Snow fall: Heavy intensity ❄️"
  elif weatherCode == "77":
    return "Snow grains ❄️"
  elif weatherCode == "80":
    return "Rain showers: Slight ☔"
  elif weatherCode == "81":
    return "Rain showers: Moderate 🌧️"
  elif weatherCode == "82":
    return "Rain showers: Violent 🌧️"
  elif weatherCode == "85":
    return "Snow showers slight ❄️"
  elif weatherCode == "86":
    return "Snow showers slight and heavy ❄️"
  elif weatherCode == "95":
    return "Thunderstorm: Slight 🌩️"
  elif weatherCode == "96":
    return "Thunderstorm with slight hail 🌩️"
  elif weatherCode == "99":
    return "Thunderstorm with heavy hail 🌩️"
  else: 
    return "The weather code was not found"

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

forecast = result.json()
weatherCode = forecast["daily"]["weathercode"][0]
temperatureMax = forecast["daily"]["temperature_2m_max"][0]
temperatureMin = forecast["daily"]["temperature_2m_min"][0]

forecast = getWeatherDescription(str(weatherCode))
print(f"{forecast}")
print(f"Temperature max 🥵: {temperatureMax} \t Temperature min 🥶: {temperatureMin}")

