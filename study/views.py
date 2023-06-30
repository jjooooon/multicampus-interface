from django.shortcuts import render, get_object_or_404, redirect
from .models import Algorithm

def index(request) :
    return render(request, 'study/algorithm.html')


def problem_list(request):
    if request.method == 'POST':
        algorithm = request.POST.get("algorithm", "없음")
        list = Algorithm.objects.order_by('-id')
        context = {'algorithm':  algorithm , 'list' : list, }
        return render(request, 'study/problem.html', context)


def detail(request, problem_id):
    problem = get_object_or_404(Algorithm, pk=problem_id)
    context = {'problem' : problem}
    return render(request, 'detail.html', context)