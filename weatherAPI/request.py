import requests

print("Welcome to the Python Weather App")
city = input("Which city's weather would you like to check? ")

url = f"https://wttr.in/{city}?format=j1"

print(f"Fetching the weather for {city}... \n")

response = requests.get(url)

if(response.status_code == 200):
    data = response.json()
    #print(data)
    condition = data['current_condition'][0]
    temp_c = condition['temp_C']
    humidity = condition['humidity']
    feelsLike = condition['weatherDesc'][0]['value']

    print(f"Temperature is: {temp_c}\n")
    print(f"humidity is: {humidity}\n")
    print(f"Currently, it is: {feelsLike}\n")

  