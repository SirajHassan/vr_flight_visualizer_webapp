from requests.models import Request
from .get_opensky_data import get_opensky_data

def update_request_data(pk):
    request = Request.objects.get(pk = pk)
    lng = request.lng
    lat = request.lat
    rad = request.rad
    json = get_opensky_data(lat,lng,rad)
    request.data = json
