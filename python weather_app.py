pip install requests
  import requests

api_key= '2643743'

city = input('London ')

url = https://www.bbc.co.uk/weather/2643743

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
