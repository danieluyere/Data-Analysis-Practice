import urllib.request, urllib.parse, urllib.error
import json
import ssl
from datetime import date, timedelta

# Handle SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service_url = 'http://py4e-data.dr-chuck.net/opengeo?'

address = input('Enter a Location: ')

if len(address) < 1:
    address = 'Minna Nigeria'

address = address.strip()
params = dict()
params['q'] = address

url = service_url + urllib.parse.urlencode(params)
# print(url) concatenate service url with the typed address

data = urllib.request.urlopen(url, context=ctx).read().decode()

info = json.loads(data)
# print(json.dumps(info, indent=4))

lat = info['features'][0]['properties']['lat']
lon = info['features'][0]['properties']['lon']

print(f'latitude: {lat} and longitude: {lon}')

#calculates paramters from present to the past 7 days
present = date.today()
past = present - timedelta(days=7)

weather_url = 'https://historical-forecast-api.open-meteo.com/v1/forecast?'
params = {
    'latitude': lat,
    'longitude': lon,
    "start_date": past,
	"end_date": present,
    'hourly': "temperature_2m"
}

url = weather_url + urllib.parse.urlencode(params)

data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)
# print(json.dumps(info, indent=4))

temps = info['hourly']['temperature_2m']
temps = [float(x) for x in temps]
max_temp = max(temps)
min_temp = min(temps)
avg_temp = round(sum(temps) / len(temps), 2)

print(f'The last 7 days in {address} has an average temperature of {avg_temp} ranging from {min_temp} to {max_temp}')