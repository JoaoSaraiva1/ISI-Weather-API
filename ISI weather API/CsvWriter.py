import requests

api_key = "MeQxuknFFZdX6228SAI9eAZK1doAjk1O"
location = "273407"

url = f"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location}"

query_string = {"apikey": api_key}

response = requests.get(url, params=query_string)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("An error occurred.")