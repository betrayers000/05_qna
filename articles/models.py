from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    user = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    content = models.CharField(max_length=100)
    # foreignkey를 이용해서 Question과 연결한다. on_delete로 상위 데이터가 삭제되면 같이 삭제한다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)