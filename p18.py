import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://py4e-data.dr-chuck.net/geojson?"

while True:
    address = input("Enter location: ")
    
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'address':address,'key':42})

    print('Retrieving',url)

    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrived',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    placeid = js["results"][0]['place_id']
    print("Place id",placeid)
