from .convert_input import convert_input
import requests
import json

def get_opensky_data(lat,lon,rad):
    #convert inputs to bounding box
    b_box= convert_input(lat,lon,rad) #returns tuple: (lat_min, long_min, lat_max, long_max)
    #build URL
    url = 'https://opensky-network.org/api/states/all?lamin='+str(b_box[0])+'&lomin='+str(b_box[1])+'&lamax='+str(b_box[2])+'&lomax='+str(b_box[3])
    #send GET request
    #response = requests.get(url)
    print("HELLOHELLO")
    print (requests.__file__)
    # data = response.text
    # parsed = json.loads(data)
    #return response.json()






#print(get_opensky_data(46.2044,6.1432,50)) #best way to print json file
