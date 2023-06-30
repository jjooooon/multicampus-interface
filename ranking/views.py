from django.shortcuts import render
from users.models import User as user_model
from .models import Ranker
import operator


def ranking(request):
    rankers = user_model.objects.all()

    for ranker in rankers:
        score = (ranker.challenge.count() * 10) + (ranker.question.count() * 10) + \
            (ranker.answer.count()*5) + ranker.challenger.count()
        ranker.score = score
        ranker.save()

    ranker_list = rankers.order_by('-score')[:5]
    context = {"rankers": ranker_list}

    return render(request, "ranking/ranking2.html", context)
