from django.shortcuts import render
from requests.models import Request
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RequestSerializer
from django.http import HttpRequest
from rest_framework.reverse import reverse

class RequestsRudView(generics.RetrieveUpdateDestroyAPIView): #DetailView CreateView FormView
	lookup_field = 'pk' #different with django 2.0, #url(r'?P<pk>\d+')
	serializer_class = RequestSerializer #converts to json and validates the data
	queryset = Request.objects.all()
	print("RUDView")
	
	def get_queryset(self):
		return Request.objects.all()

	# def list(self,request):
	# 	queryset = self.get_queryset()
	# 	serializer = RequestSerializer(queryset,many = True)
	# 	return Response(serializer.data)

	# def get(self,request,pk,format=None):
	# 	print("GETGET")
	# 	req = Request.objects.get(pk = pk)
	# 	serializer = RequestSerializer(req)
	# 	print(serializer.data)
	# 	return Response(serializer.data)





class RequestsCreateView(generics.CreateAPIView): #DetailView CreateView FormView
	lookup_field = 'pk' #different with django 2.0, #url(r'?P<pk>\d+')
	serializer_class = RequestSerializer #converts to json and validates the data
	queryset = Request.objects.all()
	print("CreateView")
	req = HttpRequest().path
	print(req)


	def get_queryset(self):
		return Request.objects.all()
