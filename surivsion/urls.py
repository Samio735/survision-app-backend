
# survey_collector_project/urls.py

from django.urls import path, include
from django.contrib import admin




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('surveys.urls')),
]
