import requests
import json

def get_weather_info(city):
    api_key = '09195acd9dfbb927b7f6b925bba707ed'
    url = f'https://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={api_key}'

    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data.get('main', {}).get('temp', 0)
        return temperature
    else:
        print(f"Error: Unable to fetch weather information. Status Code: {response.status_code}")
        return None

def display_weather_info(city, temperature):
    if temperature is not None:
        if temperature > 40:
            print(f"It's {temperature} degree celsius, thats wayyyy to HOT")
        elif temperature >= 30:
            print(f"It's {temperature} degree celsius, thats hot")
        elif temperature >= 20:
            print(f"It's {temperature} degree celsius. It's warm")
        elif temperature >= 10:
            print(f"It's {temperature} degree celsius. it's chilly outside")
        else:
            print(f" {city} too cold. Don't go.")

def main():
    for _ in range(10):
        city = input("Input city name: ")
        temperature = get_weather_info(city)
        if temperature is not None:
            display_weather_info(city, temperature)
            break
        else:
            print("Try again. Make sure that the spelling is correct.")

if __name__ == "__main__":
    main()
