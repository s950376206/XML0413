import requests
from x0413.data import Location

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url)

json_content = html_content.json()
print(json_content)

records = json_content.get('records')
location = records.get('location')
print(location)

for i in range(len(location)):
    print(location[i])

for item in location:
    lat = item.get('lat')
    lon = item.get('lon')
    locationName = item.get('locationName')
    stationId = item.get('stationId')
    time = item.get('time')
    obsTime = time.get('obsTime')
    print(lat, len, locationName, stationId, obsTime)

for item in location:
    l = Location()
    l.from_json(item)
    print(l.__dict__)

    weatherElement = item.get('weatherElement')
    for element in weatherElement:
        elementName = element.get('elementName')
        elementvalue = element.get('elementvalue')
        print(elementName, elementvalue)
