# surveys/views.py

from rest_framework import viewsets, views , response 
from rest_framework.exceptions import AuthenticationFailed
from .models import Survey, Question, Response, Choice , User
from .serializers import SurveySerializer, QuestionSerializer, ResponseSerializer, ChoiceSerializer,UserSerializer
import jwt, datetime
class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        survey_id = self.kwargs['survey_id']
        return Question.objects.filter(survey=survey_id)



class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return Choice.objects.filter(question=question_id)
    
    
class RegisterView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return response.Response(serializer.data)
        
class LoginView(views.APIView):
    def post(self,request):
        email = request.data["email"]
        password = request.data["password"]
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed("User not found!")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")
        
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload=payload, key="secret", algorithm="HS256")
        
        resp = response.Response()
        
        resp.data = {
            "jwt": token
        }
        
        resp.set_cookie(key="jwt", value=token)
        
        return resp
        

class UserView(views.APIView):
    def post(self,request):
        token = request.data["jwt"]
        
        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        
        try:
            payload = jwt.decode(jwt=token, key="secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        
        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(user)
        return response.Response(serializer.data)
    
class LogoutView(views.APIView):
    def post(self,request):
        resp = response.Response()
        resp.delete_cookie('jwt')
        resp.data = {
            "message": "success"
        }
        return resp
    
class FinishSurveyView(views.APIView):
    def post(self,request):
        token = request.data["jwt"]
        Survey_id = request.data["survey"]
        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        
        try:
            payload = jwt.decode(jwt=token, key="secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        
        user = User.objects.filter(id=payload["id"]).first()
        survey = Survey.objects.filter(id=Survey_id).first()
        survey.availableResponses -= 1
        if survey.availableResponses == 0:
            return response.Response("No available responses")
        user.credit += survey.price
        survey.save()
        user.save()
        serializer = UserSerializer(user)
        return response.Response(serializer.data)
        