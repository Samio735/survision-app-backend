# survey_collector_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from surveys.views import SurveyViewSet, QuestionViewSet, ResponseViewSet, ChoiceViewSet, RegisterView, LoginView,UserView,LogoutView,FinishSurveyView

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('surveys/<survey_id>/questions/', QuestionViewSet.as_view({'get': 'list'}), name='questions'),
    path('questions/<question_id>/choices/', ChoiceViewSet.as_view({'get': 'list'}), name='choices'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("user/", UserView.as_view(), name="user"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("finish/", FinishSurveyView.as_view(), name="finish"),
]
