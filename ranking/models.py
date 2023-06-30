from tkinter import scrolledtext
from django.db import models
from users import models as user_models


class Ranker (models.Model):
    rankers = models.ManyToManyField(
        user_models.User, related_name="ranking")
    score = models.IntegerField(default=0)
