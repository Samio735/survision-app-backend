
# survey_collector_project/urls.py

from django.urls import path, include

from . import views



urlpatterns = [
    path('', views.api_home),
]
