from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        req = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=fc4835916d554965b6eb76b55e5ce543').read()
        json_data = json.loads(req)
        data = {
            "country_code":str(json_data['sys']['country']),
            "coordinates":str(json_data['coord']['lon']) + ' '+str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'K',
            "pressure":str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city=''
        data = {}

    return render(request, 'index.html', {'city':city, 'data':data})