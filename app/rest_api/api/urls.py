from django.urls import include, path, register_converter
from rest_framework import routers
from .views import UserRequestsRudView, UserRequestsCreateView
from . import converters, views


register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [
   path('<int:pk>',UserRequestsRudView.as_view(),name='user-request-rud'),
   path('lat=<float:lat>&lon=<float:lon>&rad=<int:rad>',UserRequestsCreateView.as_view(),name='user-request-create'),
]
