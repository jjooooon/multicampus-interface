from django.shortcuts import render, redirect
from .models import Maps
from .forms import MapsForm


def index(request):
    map = Maps.objects.order_by('-id')
    context = {'map': map}
    return render(request, 'map/info.html', context)


def map_create(request):
    if request.method == 'POST':
        form = MapsForm(request.POST)
        if form.is_valid():
            map = form.save()
            map.save()
            return redirect('/map/')
    else:
        form = MapsForm()
        context = {'form': form}
    return render(request, 'map/cafe_create.html', context)


def map_notebook(request):
    map = Maps.objects.order_by('-id')
    context = {'map': map}
    return render(request, 'map/map_notebook.html', context)


def map_study(request):
    map = Maps.objects.order_by('-id')
    context = {'map': map}
    return render(request, 'map/map_study.html', context)
