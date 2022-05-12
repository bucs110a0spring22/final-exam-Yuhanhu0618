import requests

class GeoAPI:
  def __init__(self, location=""):
    '''
    Initialize the URL for the API
    args (str): Takes in the location name from the user input
    return: None
    '''
    self.url = f"http://dev.virtualearth.net/REST/v1/Locations/{location}%2098052?&key=AoizkyBvC8A-JiYi9I3j9N1e8tlyDFE9kR0bJ2OmgLBWOL4VURa-vXrV4z48YqnO"

  def get(self):
    '''
    Get the longitude and latitude of the inputed location
    args: None
    return (list): Return the longitude and latitude of the location
    '''
    r = requests.get(self.url)
    data = r.json()
    coord = data.get("resourceSets")[0].get("resources")[0].get("point").get("coordinates")
    return coord