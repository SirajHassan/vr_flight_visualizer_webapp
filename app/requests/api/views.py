from django.shortcuts import render
from requests.models import Request
from rest_framework import generics
from .serializers import RequestSerializer

class RequestsRudView(generics.RetrieveUpdateDestroyAPIView): #DetailView CreateView FormView
	lookup_field = 'pk' #different with django 2.0, #url(r'?P<pk>\d+')
	serializer_class = RequestSerializer #converts to json and validates the data
	queryset = Request.objects.all()
	print("RUDView")
	print(queryset)

	def get_queryset(self):
		return Request.objects.all()


class RequestsCreateView(generics.CreateAPIView): #DetailView CreateView FormView
	lookup_field = 'pk' #different with django 2.0, #url(r'?P<pk>\d+')
	serializer_class = RequestSerializer #converts to json and validates the data
	queryset = Request.objects.all()
	print("CreateView")
	print(queryset)

	def get_queryset(self):
		return Request.objects.all()
