#Inputs will be latitude, longitude and radius.
#Outputs will be a tuple (lat_min, long_min, lat_max, long_max)
from geolocation import GeoLocation

def convert_input(lat,long,radius):
     loc = GeoLocation.from_degrees(lat, long)
     distance = radius/2
     SW_loc, NE_loc = loc.bounding_locations(distance)
     lat_min = SW_loc.deg_lat
     long_min = SW_loc.deg_lon
     lat_max = NE_loc.deg_lat
     long_max = NE_loc.deg_lon
     return (lat_min,long_min,lat_max,long_max)


#print(convert_input(0,0,100))
