import requests
import json
import time


def open_sky_request(lat,lng,radius,url):

	#TODO: convert lat/lng and radius into a square.. or find a different http REST request 
	# were going to want an id with each user and the request they are sending.. 
	#https://opensky-network.org/apidoc/rest.html
	response = requests.get(url)
	data = response.text
	return(data)


#testing..
count = 1
while(1):
	count = count +1
	time.sleep(.001)
	url = "https://opensky-network.org/api/states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226"
	print(open_sky_request(42.332,7.1095,50,url))
	print(count)




	










