from django.urls import include, path
from rest_framework import routers
from .views import RequestsRudView, RequestsCreateView

urlpatterns = [
   path('<int:pk>/',RequestsRudView.as_view(),name='request-rud'),
   path('',RequestsCreateView.as_view(),name='request-create'),
]
