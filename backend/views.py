from rest_framework.views import APIView , status
from rest_framework.response import Response
from .serializer import authserializer
from .models import Auth,quiz_available,questions,S_details,q_details
from .serializer import authserializer,questionSerializer,S_detailsserializer,detailsserializer
from rest_framework.authtoken.models import Token
from .models import Auth

class authentication(APIView):
	def post(self,request):
		pasw=Auth.objects.get(userid=request.data.get('userid','')).password
		print("pasw is " + str(pasw))
		if pasw==request.data.get('password',''):
			return Response("ok")
		return Response(status=status.HTTP_403_FORBIDDEN)

class quiz(APIView):

	def get(self,request):
		quest=questions.objects.all()
		print(quest)
		serializer=questionSerializer(quest,many=True)
		return Response(serializer.data)

	def post(self,request):
		subject_code = request.data.get('subject_code', '')
		ques = request.data.get('ques', '')
		opt1 = request.data.get('opt1', '')
		opt2 = request.data.get('opt2', '')
		opt3 = request.data.get('opt3', '')
		opt4 = request.data.get('opt4', '')
		correct = request.data.get('correct', '')
		subject_code = request.data.get('subject_code', '')
		#print("Working fine" + opt1)
		obj = questions(subject_code=subject_code, ques=ques, opt1=opt1, opt2=opt2, opt3=opt3, opt4=opt4,correct=correct)
		obj.save()
		return Response("ok")

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
