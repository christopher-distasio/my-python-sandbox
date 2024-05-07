import requests

# API and city setup
API_URL = 'https://goweather.herokuapp.com/weather/'
city = 'seattle'

# Fetch data
response = requests.get(API_URL + city).json()

# Output fetched data
print("Fetched Weather Data:", response)
