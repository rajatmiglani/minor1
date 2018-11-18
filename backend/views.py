from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import authserializer
from .models import Auth,quiz_available,questions,S_details,q_details
from .serializer import authserializer,questionSerializer,S_detailsserializer,detailsserializer
from rest_framework.authtoken.models import Token
from .models import Auth

class authentication(APIView):
	def validate(self,request):
		pasw=Auth.objects.get(userid="username")
		if pasw=="password":
			qz=quiz_available.objects.all()
			serializer=authserializer(qz,many=True)
			return Response(serializer.data)

class quiz(APIView):
	def get(self,request):
		quest=questions.objects.all()
		serializer=questionSerializer(quest,many=True)
		return Response(serializer.data)

class batchdetails(APIView):
	def det(self,request):
		var=S_details.objects.all()
		serializer=S_detailsserializer(var,many=True)
		return Response(serializer.data)

class submit_marks(APIView):
	def sumMarks(self,request):
		userid=request.POST.get('userid','')
		batch=request.POST.get('batch','')
		subject_code=request.POST.get('subject_code','')
		marks=request.POST.get('marks','')
		quiz_instance=request.POST.get('quiz_instance','')
		obj=S_detailsserializer(userid=userid,batch=batch,subject_code=subject_code,marks=marks,quiz_instance=quiz_instance)
		obj.save()

def question(request):
	if request.method=='POST':
		ques=request.POST.get('ques','')
		opt1=request.POST.get('opt1','')
		opt2=request.POST.get('opt2','')
		opt3=request.POST.get('opt4','')
		opt4=request.POST.get('opt4','')
		correct=request.POST.get('correct','')
		subject_code=request.POST.get('subject_code','')
		obj=questions(subject_code=subject_code,ques=ques,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4,correct=correct)
		obj.save()
