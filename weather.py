from pyowm import OWM
from geopy.geocoders import Nominatim
import requests
import keyInfo

owm = OWM(keyInfo.key)
mng = owm.weather_manager()
geolocator = Nominatim(user_agent="geoapiExercises")

results = []

def get_forecasts(lat, lon):
    #observation = mng.three_hours_forecast_at_coords(lat, lon)
    #Forecasts = mng.forecast_at_coords(lat, lon, "3h").forecast
    #Forecasts = mng.three_hours_forecast(lat, lon, "3h")
    #forecasts = Forecasts.most_hot()


    location = geolocator.reverse(str(lat)+","+str(lon))
    address = location.raw['address']

    city = address.get('city', '')
    #state = address.get('state', '')
    country = address.get('country', '')
    #code = address.get('country_code')
    zipcode = address.get('postcode')

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}"
    response = requests.get(url).json()
    for i in range(len(response['list'])):
        basic_info = response['list'][i]['main']
        weather_info = response['list'][i]['weather'][0]
        wind_info = response['list'][i]['wind']
        temp = basic_info['temp']
        feel_like = basic_info['feels_like']
        temp_min = basic_info['temp_min']
        temp_max = basic_info['temp_max']
        humidity = basic_info['humidity']
        weather = weather_info['main']
        wind_speed = wind_info['speed']
        dateTime = response['list'][i]['dt_txt']

        results.append("""
        City: {} 
        Latitude : {} , Longitude: {}
        Zip Code: {}
        Country: {}
        Time : {}
        Temperature : {} degree Celcius
        Feels like: {} degree Celcius
        Min Temperature : {} degree Celcius
        Max Temperature : {} degree Celcius
        Humidity: {}
        Probable Weather: {}
        Wind Speed: {}
        """.format(city, lat, lon, zipcode, country, dateTime,
                   int(temp)-273.16, int(feel_like)-273.16, int(temp_min)-273.16, int(temp_max)-273.16,
                   humidity,weather,wind_speed))

    return "".join(results[:10])