from django.shortcuts import render
from .models import CityName
import requests
import json
def home(request):
    return render(request, 'index.html')

def wth(request):
    if request.GET['c_name']:
        name=str(request.GET['c_name'])
    else:
        return render(request,'not_found.html')
    
    
    api_key='8edfbffb61c67105f1b971ffc1272c4a'
    units='metric'
    city_name=name
    get_request_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units={units}&appid={api_key}'

    response_json=requests.get(get_request_url).json()

    if response_json['cod'] != 200:
        return render(request,'not_found.html')


    response_name=response_json['name']
    response_country=response_json['sys']['country']

    temperature_in_celsius=response_json['main']['temp']
    wind_speed_in_kmph=response_json['wind']['speed']
    humidity_in_percentage=response_json['main']['humidity'] 
    pressure=response_json['main']['pressure']
    main_info=response_json['weather'][0]['main']
    response_icon=response_json['weather'][0]['icon']
    description=response_json['weather'][0]['description']


    context={'name':response_name,
            'country':response_country,
            'temp':temperature_in_celsius,
            'wind':wind_speed_in_kmph,
            'hum':humidity_in_percentage,
            'p':pressure,
            'info':main_info,
            'des':description,
            'icon':response_icon,
    }

    
    # context={'name':'CityName',
    #         'country':'Country',
    #         'temp':'45 C',
    #         'wind':'50mph',
    #         'hum':'45%',
    #         'p':'500br',
    #         'info':'riny',
    #         'des':'heavy Rain ',
    #         'icon':'ICon',
    # }
    return render(request,'res.html',context)
