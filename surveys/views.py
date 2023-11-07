from django.shortcuts import render
#import json response
from django.http import JsonResponse

# Create your views here.

def api_home(request):
    return JsonResponse({'info': 'Django REST API', 'name': 'survey_collector_project', 'version': '1.0.0', 'author': 'Sergio Sanchez'})