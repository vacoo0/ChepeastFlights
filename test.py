from FlightRadar24 import FlightRadar24API
fr_api = FlightRadar24API()
import requests
# zones = fr_api.get_zones()
# print(zones)
# airports = fr_api.get_airports()
# print(airports)

# lukla_airport = fr_api.get_airport(code = "DUB", details = True)
# print(lukla_airport)
city_name = 'Dublin'
api_key = "db6195ca9e7f0b72cd82cc503284158f"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(weather_url)
weather_data = response.json()
print(weather_data)
