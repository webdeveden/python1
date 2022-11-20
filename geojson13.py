# this code will use json to use google map service on a specified address

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#api_key = False
# If you have a Google Places API key, enter it here

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address= input('Enter location:')
    if len(address) < 1: break

    url= serviceurl + urllib.parse.urlencode({'address': address}) # this turn the address in the url with +(space), 2c(,)

    print('Retrieving', url)
    uh= urllib.request.urlopen(url, context= ctx)
    data= uh.read().decode()
    print('Retrieved',len(data),'characters')

    try:
        js= json.loads(data)
    except:
        js= None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        break
    lat= js["results"][0]["geometry"]["location"]["lat"]
    lng= js["results"][0]["geometry"]["location"]["lng"]
    print("Lat:",lat,"Lng:",lng)
    location= js["results"][0]["formatted_address"]
    print(location)
