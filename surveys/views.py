# surveys/views.py

from rest_framework import viewsets
from .models import Survey, Question, Response, Choice
from .serializers import SurveySerializer, QuestionSerializer, ResponseSerializer, ChoiceSerializer

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