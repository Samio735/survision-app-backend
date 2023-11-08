# surveys/models.py

from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    title = models.CharField(max_length=255)
    availableResponses = models.IntegerField(default=0)
    allResponses = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    # Add other survey-related fields
    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    # Add other question-related fields
    def __str__(self):
        return self.survey.title + " : " + self.text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    # make the title the text of the choice and the name of question
    def __str__(self):
        return self.question.text + " : " + self.text 

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    
    # Add other response-related fields
    def __str__(self):
        return self.choice.text

class Credit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username + " : " + str(self.amount)
