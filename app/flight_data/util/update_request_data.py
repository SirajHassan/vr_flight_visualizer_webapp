from rest_api.models import UserRequest
from .get_opensky_data import get_opensky_data

def update_request_data(pk):
    print("update_request_data")
    req = UserRequest.objects.get(pk = pk)
    lat = req.lat
    lng = req.lng
    rad = req.rad
    json = get_opensky_data(lat,lng,rad)
    print(json)
    req.data = json
    req.save()
    print("req_data")
    print(req.data)
