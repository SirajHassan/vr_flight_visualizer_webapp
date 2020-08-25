from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import JSONField

from rest_framework.reverse import reverse as api_reverse



class Request(models.Model):
	# user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	lat = models.DecimalField( max_digits = 10, decimal_places = 5, null = True, blank = True)
	lng = models.DecimalField( max_digits = 10, decimal_places = 5, null = True, blank = True )
	timestamp = models.DateTimeField(auto_now_add = True)
	data = JSONField(null=True, blank=True)

	# def __str__(self):
	# 	return str(self.user)
