import requests

def weather_forecast():
    url='https://api.openweathermap.org/data/2.5/forecast?q=celina&appid=989f9145125504f3fa2a7a22b49ea2d1'
    weather=requests.get(url)
    output=weather.json()
    items=output['list']
    city=output['city']['name']
    print('City,Time,Temparature,Condition')
    for item in items:
        print(city + "," + item['dt_txt'] + "," + str(item['main']['temp']) +  "," + item['weather'][0]['description'])

weather_forecast()