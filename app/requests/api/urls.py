from django.urls import include, path, register_converter
from rest_framework import routers
from .views import RequestsRudView, RequestsCreateView
from . import converters, views


register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [
   path('<int:pk>',RequestsRudView.as_view(),name='request-rud'),
   path('lat=<float:lat>&long=<float:lon>&rad=<int:rad>&id=<int:id>',RequestsCreateView.as_view(),name='request-create'),
]
