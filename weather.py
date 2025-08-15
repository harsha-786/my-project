# 1. Import the necessary libraries
import requests
import os # Often useful for handling environment variables for API keys

# 2. Set up your API key and the city you want to check
# It's better practice to load this from an environment variable, but for now, we'll put it here.
# IMPORTANT: Replace "YOUR_API_KEY_HERE" with the key you copied.
API_KEY = "b3ea9007168bce4d9f596aeb4954205b" 
city_name = input("Enter city name: ")

# 3. Construct the API request URL
# The f-string lets us easily embed our variables into the URL string.
base_url = "http://api.openweathermap.org/data/2.5/weather"
api_url = f"{base_url}?q={city_name}&appid={API_KEY}&units=metric"

try:
    # 4. Make the API request
    # requests.get() sends a request to the server and gets the response back.
    response = requests.get(api_url)
    response.raise_for_status() # This will raise an error for bad responses (4xx or 5xx)

    # 5. Parse the JSON response
    # The response from the API is in a format called JSON. 
    # The .json() method converts this text into a Python dictionary.
    data = response.json()

    # 6. Extract and display the relevant information
    # We navigate the dictionary to find the data we need.
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    
    print(f"\nCurrent weather in {city_name.title()}:")
    print(f"Description: {weather_description.capitalize()}")
    print(f"Temperature: {temperature}°C")

except requests.exceptions.HTTPError as err:
    if response.status_code == 401:
        print("Error: Invalid API Key. Please check your key and try again.")
    elif response.status_code == 404:
        print(f"Error: City '{city_name}' not found.")
    else:
        print(f"An HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
