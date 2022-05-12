from EarthquakeAPI import EarthquakeAPI
from GeoAPI import GeoAPI

def main():
  data = str(input("Please enter a place on Earth:\n"))
  inputLocation = data.replace(" ", "%20")
  location = GeoAPI(inputLocation)
  coord = location.get()
  maxradius = input("Please enter your desired search radius in kilometers: (max=20001)\n")
  earthAPI = EarthquakeAPI(coord[0], coord[1], maxradius)
  quakeNum = earthAPI.get()
  print("There's " + str(quakeNum) + " earthquakes in " + data)
  

main()