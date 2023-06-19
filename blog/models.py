from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

class Question(models.Model):
    qusetion_text = models.CharField(max_length=200)
    time = models.DateTimeField()
    
class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    