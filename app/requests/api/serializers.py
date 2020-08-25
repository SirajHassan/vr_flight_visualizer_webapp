from rest_framework import serializers
from requests.models import Request


class RequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Request
		fields = [
			'pk',
			# 'user',
			'lat',
			'lng',
			'timestamp',
			'data'
		]
		extra_kwargs = {'user': {'required': False}}
