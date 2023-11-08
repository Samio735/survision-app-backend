from django.contrib import admin

# Register your models here.

from .models import Survey, Question, Response, Choice, Credit

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Choice)
admin.site.register(Credit)

