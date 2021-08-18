from django.db import models

# Create your models here.
class Response(models.Model):
    
    name = models.CharField(max_length=10)
    gubun = models.IntegerField()
    question1 = models.IntegerField()
    question2 = models.IntegerField()
    question3 = models.IntegerField()
    question4 = models.IntegerField()
    question5 = models.IntegerField()
    question6 = models.IntegerField()
    question7 = models.IntegerField()
    question8 = models.IntegerField()
    question9 = models.IntegerField()
    question10 = models.IntegerField()
    kk1 = models.IntegerField()
    reg_date = models.DateTimeField()