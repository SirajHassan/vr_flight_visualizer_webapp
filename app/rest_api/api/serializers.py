from rest_framework import serializers
from rest_api.models import UserRequest


class UserRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserRequest
		fields = [
			'pk',
			# 'user',
			'lat',
			'lng',
			'timestamp',
			'data'
		]
