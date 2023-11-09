# surveys/models.py

from django.db import models
from django.contrib.auth.models import   AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=False,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    credit = models.IntegerField(default=0)
    objects = CustomUserManager()
    


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




# users/models.py





