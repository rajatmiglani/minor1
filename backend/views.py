from rest_framework.views import APIView , status
from rest_framework.response import Response
from .models import Auth,quiz_available,questions,S_details,q_details,subjects
from .serializer import questionSerializer,S_detailsserializer,detailsserializer,quiz_availableSerializer
from rest_framework.authtoken.models import Token
from .models import Auth

class authentication(APIView):
	def post(self,request):
		pasw=Auth.objects.get(userid=request.data.get('userid','')).password
		print("pasw is " + str(pasw))
		if pasw==request.data.get('password',''):
			return Response("ok")
		return Response(status=status.HTTP_403_FORBIDDEN)	

#name is quiz available but subjects and subject_code are taken from subjects model(check serializer)
class quizavailable(APIView):
	def get(self,request):
		available=subjects.objects.all()
		print(available)
		serializer=quiz_availableSerializer(available,many=True)
		return Response(serializer.data)

class quizStudents(APIView):
	def post(self,request):
		question=questions.objects.filter(subject_code=request.data.get('subject_code',''))
		print(question)
		serializer=questionSerializer(question,many=True)
		return Response(serializer.data)
		
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

#marks table
class batchdetails(APIView):
	def get(self,request):
		var=S_details.objects.all()
		serializer=S_detailsserializer(var,many=True)
		return Response(serializer.data)

#to submit marks of students in table (check instatance field once)
class submit_marks(APIView):
	def post(self,request):
		userid=request.data.get('userid','')
		name=request.data.get('name','')
		batch=request.data.get('batch','')
		subject_code=request.data.get('subject_code','')
		marks=request.data.get('marks','')
		#quiz_instance=request.data.get('quiz_instance','')
		obj=S_details(name=name,userid=userid,batch=batch,subject_code=subject_code,marks=marks)
		obj.save()
		return Response("ok")
