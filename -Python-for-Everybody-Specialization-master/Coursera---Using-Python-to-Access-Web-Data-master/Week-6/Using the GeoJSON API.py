'''
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://python-data.dr-chuck.net/geojson
This API uses the same parameters (sensor and address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.pythonlearn.com/code/geojson.py
'''
import time
start = time.time()
import urllib.request, urllib.parse, urllib.error
import json

#Api
api = 'http://py4e-data.dr-chuck.net/geojson?'

#Input data
link = input('Enter location: ')
link = api + urllib.parse.urlencode({'address':link})
print('Retrieving', link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    js = json.loads(html)
except:
    js = None

placeId = js['results'][0]['place_id']
print('Place id', placeId)
end = time.time()

print("The total excecution Time for this code is sec", (end-start))

'''
Enter location: Simon Fraser University
Retrieving http://py4e-data.dr-chuck.net/geojson?address=Simon+Fraser+University
Retrieved 2365 characters
Place id ChIJa8FTJPrzBFMR8dy-IfiXGMA
The total excecution Time for this code is sec 2.1262848377227783

'''
