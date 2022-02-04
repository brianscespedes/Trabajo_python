from django.shortcuts import render
from backend.models import *


def index(request):
    return render(request, 'frontend/index.html', {
        'user': request.user,
        'courses': Course.objects.all(),
        'students': Student.objects.all(),
    })


def matriculas(request):
    return render(request, 'frontend/matriculas.html', {
        'user': request.user,
        'matriculas': Course.objects.all(),
    })


def nueva_matricula(request):
    return render(request, 'frontend/matriculas.html', {
        'user': request.user,
        'matriculas': Course.objects.all(),
    })
