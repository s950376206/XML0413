class Location:
    def __init__(self, location_name=None, lat=None, lon=None,
                 station_id=None, time=None, weather_element=None):
        self.locationName = location_name
        self.lat = lat
        self.lon = lon
        self.stationId = station_id
        self.time = time

    def from_json(self, json_data):
        self.lat = json_data.get('lat')
        self.lon = json_data.get('lon')
        self.locationName = json_data.get('locationName')
        self.station_id = json_data.get('stationId')
        time = json_data.get('time')
        self.time = time.get('obsTime')