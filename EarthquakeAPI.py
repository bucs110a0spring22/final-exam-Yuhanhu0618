import requests

class EarthquakeAPI:
  def __init__(self, latitude = 0, longitude = 0, maxradiuskm = 20000):
    '''
    Initialize the URL
    args (int): Takes in the latitude, logitude, and max radius in km from the GeoAPI
    return: None
    '''
    self.url = f"https://earthquake.usgs.gov/fdsnws/event/1/count?format=geojson&latitude={latitude}&longitude={longitude}&maxradiuskm={maxradiuskm}"

  def get(self):
    '''
    Request data from the API and get it as a json file
    args: None
    return (int): Return the number of earthquake ever happened in this area (a circle using the max raidus and the place inputed is the center).
    '''
    r = requests.get(self.url)
    data = r.json()
    return data.get("count")