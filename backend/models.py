from django.db import models

class Auth(models.Model):
	userid=models.IntegerField(unique=True)
	password=models.CharField(max_length=10)

class subjects(models.Model):
	subject_name=models.CharField(max_length=10)
	subject_code=models.CharField(max_length=10)

class q_details(models.Model):
	subject_code=models.CharField(max_length=10)
	fname=models.CharField(max_length=50)
	batch=models.CharField(max_length=2)
	quiz_instance=models.CharField(max_length=4)

class S_details(models.Model):
	name=models.CharField(max_length=40)
	userid=models.IntegerField(unique=True)
	batch=models.CharField(max_length=2)
	subject_code=models.CharField(max_length=10)
	marks=models.IntegerField()
	quiz_instance=models.CharField(max_length=4)	

class quiz_available(models.Model):
	quiz_name=models.CharField(max_length=4)

class questions(models.Model):
	subject_code=models.CharField(max_length=10)
	ques=models.CharField(max_length=150)
	opt1=models.CharField(max_length=50)
	opt2=models.CharField(max_length=50)
	opt3=models.CharField(max_length=50)
	opt4=models.CharField(max_length=50)
	correct=models.IntegerField()