from django.shortcuts import render
from rest_api.models import UserRequest
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserRequestSerializer
from django.http import HttpRequest
from django.http import HttpResponse
from rest_framework.reverse import reverse
from flight_data.util import pythonRQ_test
from flight_data.util import worker

class UserRequestsRudView(generics.RetrieveUpdateDestroyAPIView): #DetailView CreateView FormView
	lookup_field = 'pk' #different with django 2.0, #url(r'?P<pk>\d+')
	serializer_class = UserRequestSerializer #converts to json and validates the data
	queryset = UserRequest.objects.all()
	print("RUDView")

	def get_queryset(self):
		return UserRequest.objects.all()


class UserRequestsCreateView(generics.CreateAPIView):
	lookup_field = 'pk'
	serializer_class = UserRequestSerializer
	queryset = UserRequest.objects.all()
	print(UserRequest.id)
	print("CreateView")
	req = HttpRequest().path
	print(req)


	def create(self, request,lat,lon,rad):
		print ("creating...")
		print(lat)
		print(lon)
		print(rad)
		new_req = UserRequest(lat = lat, lng = lon, rad = rad)
		new_req.save()

		#python RQ worker
		pythonRQ_test.test(new_req.pk)
		worker.run()


		return HttpResponse(str(new_req.pk))


	def get_queryset(self):
		return UserRequest.objects.all()
