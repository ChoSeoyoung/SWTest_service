from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 50)
    create_date = models.DateTimeField()
    content = models.TextField()
    ans1 = models.TextField()
    ans2 = models.TextField()
    ans3 = models.TextField()
    ans4 = models.TextField()
    ans = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
