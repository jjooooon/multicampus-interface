from django.db import models
from users import models as user_models

class Recruit(models.Model):
    COMPETITION_CHOICES=[
        ('2022년 강서구 빅데이터 활용 공모전', '2022년 강서구 빅데이터 활용 공모전'),
        ('2022년 빅데이터캠퍼스 멘토링 멘티 모집', '2022년 빅데이터캠퍼스 멘토링 멘티 모집'),
    ]
    author = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    select = models.CharField(max_length=80, choices=COMPETITION_CHOICES, null=True)
    personnel = models.IntegerField(default=0)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject



class Applicant(models.Model):
    author = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    question = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)



class Comment(models.Model):
    author = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Recruit, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Applicant, null=True, blank=True, on_delete=models.CASCADE)