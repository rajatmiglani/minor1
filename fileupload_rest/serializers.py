from rest_framework import serializers
from backend.models import Uploadfile

class uploadfileserializer(serializers.ModelSerializer):
	class Meta:
		model=Uploadfile
		fields=('pk','file',)