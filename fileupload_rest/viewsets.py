from rest_framework import viewsets
from fileupload_rest.serializers import uploadfileserializer
from backend.models import Uploadfile

class Uploadfileviewset(viewsets.ModelViewSet):
	queryset=Uploadfile.objects.all()
	serializer=uploadfileserializer