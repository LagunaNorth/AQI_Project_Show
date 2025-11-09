import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')

def load_air_data(city):
    response = requests.get(API_URL, params={'key': API_KEY, 'q': city, 'days': 3, 'aqi': 'yes'})
    data = response.json()
    city_name = data['location']['name']
    aqi = data['current']['air_quality']['us-epa-index']        
    forecast_hours0 = data['forecast']['forecastday'][0]['hour']
    hours = [hour['time'][-5:] for hour in forecast_hours0]
    co = [hour['air_quality']['co'] for hour in forecast_hours0]
    no2 = [hour['air_quality']['no2'] for hour in forecast_hours0]
    o3 = [hour['air_quality']['o3'] for hour in forecast_hours0]
    so2 = [hour['air_quality']['so2'] for hour in forecast_hours0]
    pm2_5 = [hour['air_quality']['pm2_5'] for hour in forecast_hours0]
    pm10 = [hour['air_quality']['pm10'] for hour in forecast_hours0]
    forecast_hours1 = data['forecast']['forecastday'][1]['hour']
    hours1 = [hour['time'][-5:] for hour in forecast_hours1]
    co_1 = [hour['air_quality']['co'] for hour in forecast_hours1]
    no2_1 = [hour['air_quality']['no2'] for hour in forecast_hours1]
    o3_1 = [hour['air_quality']['o3'] for hour in forecast_hours1]
    so2_1 = [hour['air_quality']['so2'] for hour in forecast_hours1]
    pm2_5_1 = [hour['air_quality']['pm2_5'] for hour in forecast_hours1]
    pm10_1 = [hour['air_quality']['pm10'] for hour in forecast_hours1]
    forecast_hours2 = data['forecast']['forecastday'][2]['hour']
    hours2 = [hour['time'][-5:] for hour in forecast_hours2]
    co_2 = [hour['air_quality']['co'] for hour in forecast_hours2]
    no2_2 = [hour['air_quality']['no2'] for hour in forecast_hours2]
    o3_2 = [hour['air_quality']['o3'] for hour in forecast_hours2]
    so2_2 = [hour['air_quality']['so2'] for hour in forecast_hours2]
    pm2_5_2 = [hour['air_quality']['pm2_5'] for hour in forecast_hours2]
    pm10_2 = [hour['air_quality']['pm10'] for hour in forecast_hours2]
    def show_aqi(aqi):
        if aqi == 1:
            return ('😃 хорошее*')
        elif aqi == 2:
            return ('🙂 среднее*')
        elif aqi == 3:
            return('😐 нездоровое для чувствительных групп*')
        elif aqi == 4:
            return ('😖 нездоровое*')
        elif aqi == 5:
            return ('😷 очень нездоровое*')
        else:
            return ('☣️ опасное*')
    aqi_level = show_aqi(aqi)

    return {
        'city_name': city_name,
        'aqi' : aqi,
        'aqi_level' : aqi_level,
        'hours': hours,
        'co' : co,
        'no2': no2,
        'o3' : o3,
        'so2' : so2,
        'pm2_5' : pm2_5,
        'pm10' : pm10,
        'hours1': hours1,
        'co_1' : co_1,
        'no2_1': no2_1,
        'o3_1' : o3_1,
        'so2_1' : so2_1,
        'pm2_5_1' : pm2_5_1,
        'pm10_1' : pm10_1,
        'hours2': hours2,
        'co_2' : co_2,
        'no2_2': no2_2,
        'o3_2' : o3_2,
        'so2_2' : so2_2,
        'pm2_5_2' : pm2_5_2,
        'pm10_2' : pm10_2,
        }
