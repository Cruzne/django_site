from django.db import models

class Question(models.Model):
    question_text = models.charfield(max_length=200)
    pub_date = models.DatetimeField('date published')

class Choice(models.Model):
    question = models.foreignkey(Question, on_delete=models.casdade)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
