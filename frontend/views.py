from django.shortcuts import render
from backend.models import *
from django.forms import modelform_factory


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
        'form': modelform_factory(Student, fields="__all__"),
    })


def nueva_matricula(request):
    return render(request, 'frontend/matriculas.html', {
        'user': request.user,
        'form': modelform_factory(Student, fields="__all__"),
    })
