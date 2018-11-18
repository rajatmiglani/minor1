from rest_framework import serializers
from backend import models
from backend.models import Auth,subjects,q_details,S_details,quiz_available,questions
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class authserializer(serializers.ModelSerializer):
	class Meta:
		model=quiz_available
		fields='_all_'

class questionSerializer(serializers.ModelSerializer):
	class Meta:
		model=questions
		fields=('ques',
			'opt1',
			'opt2',
			'opt3',
			'opt4',
			'correct')

class S_detailsserializer(serializers.ModelSerializer):
	class Meta:
		model=S_details
		fields=(
			'name',
			'userid',
			'batch',
			'subject_code',
			'quiz_instance'
			'marks'
		)

class detailsserializer(serializers.ModelSerializer):
	class Meta:
		model=q_details
		fields=(
			'subject_code',
			'batch',
			'quiz_instance'
		)

